from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from ..models import User,Places,Favorites
from flask_login import current_user,login_required
import json
from ..requests import create_stop_locations_details,get_from_database,get_route
from geojson import Point, Feature


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



@main.route('/favourites')
@login_required
def favourites():

    user = current_user

    title = current_user.name

    places = Places.query.all()

    for place in places:
        new_route = {"lat": place.lat, "long": place.lng, "name": place.place_name, "is_stop_location": True}
        get_from_database(new_route)

    return render_template('favourites.html',title=title, user = user, places = places)




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



@main.route('/explore')
def home():
    title = 'Explore'

    user = current_user

    places = Places.query.all()

    for place in places:
        new_route = {"lat": place.lat, "long": place.lng, "name": place.place_name, "is_stop_location": True}
        get_from_database(new_route)

    route = get_route()

    stop_locations = create_stop_locations_details(route)

    return render_template('home.html',title=title,stop_locations=stop_locations, user = user, ACCESS_KEY='sk.eyJ1Ijoic2FiZXJkYW5nZXIiLCJhIjoiY2pzZWJjZ3JwMTI0ZDN6bWx4bHplcWl3dyJ9.8EJHp44K185MRZExZcv_Tg',places=places)

@main.route('/like/<int:id>')
def like(id): 

    place = Places.query.get_or_404(id)

    has_faved = Favorites.query.filter_by(user_id=current_user.id,place_id=place.id).first()

    if has_faved:
        db.session.delete(has_faved)
        db.session.commit()
    else:
        fav = Favorites(place_id=place.id,user_id=current_user.id)
        db.session.add(fav)
        db.session.commit()

    

    


    return redirect(url_for('main.favourites'))