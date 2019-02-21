from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from flask_login import current_user,login_required
import json


@main.route('/')
def index():
   title = 'Vybe'
   return render_template('index.html',title=title)

@main.route('/profile')
@login_required
def profile():

   user = current_user

   title = current_user.name

   return render_template('profile.html',title=title, user = user)


@main.route('/places.geojson')
def places_json():
    """Send places data for map layer as Geojson from database.
        Will require some review.
    """

    features = []


    for place in Places.query.all():
        # get the first image of a place, if any
        image = ""
        if len(place.images) > 0:
            image = place.images[0].imageurl 
        # get the average rating of a place
        avg_rating = ""
        rating_scores = [r.user_score for r in place.ratings]
        if len(rating_scores) > 0:
            avg_rating = float(sum(rating_scores))/len(rating_scores)
        
        features.append({
                        "type": "Feature",
                        "properties": {
                            "name": place.place_name,
                            "description": place.place_description
                            # "artist":  place.place_artist,
                            # "display-dimensions": place.place_display_dimensions,
                            # "location-description": place.place_location_description,
                            # "medium": place.place_medium
                            },
                        "geometry": {
                            "coordinates": [
                                place.lng,
                                place.lat],
                            "type": "Point"
                        },
                        "id": place.place_id,
                        'image': image,
                        'avg_rating': avg_rating,
                        })
    
    places_geojson = {
                        "type": "FeatureCollection",
                        "features": features,
                        }

    return jsonify(places_geojson)


