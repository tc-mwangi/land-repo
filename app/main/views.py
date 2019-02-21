from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from ..models import User,Places
from flask_login import current_user,login_required
import json
from ..requests import create_stop_locations_details
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

   stop_locations = create_stop_locations_details()

   return render_template('favourites.html',title=title, user = user, stop_locations = stop_locations)




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

    ROUTE = [{"lat": 64.0027441, "long": -22.7066262, "name": "Keflavik Airport", "is_stop_location": True}]
    # for place in places:
    #     details = {"lat": 64.0027441, "long": -22.7066262, "name": "Keflavik Airport", "is_stop_location": True}
    #     ROUTE.append(details)
    

    # Mapbox driving direction API call
    ROUTE_URL = "https://api.mapbox.com/directions/v5/mapbox/driving/{0}.json?access_token={1}&overview=full&geometries=geojson"

    def create_route_url():
        # Create a string with all the geo coordinates
        lat_longs = ";".join(["{0},{1}".format(point["long"], point["lat"]) for point in ROUTE])
        # Create a url with the geo coordinates and access token
        url = ROUTE_URL.format(lat_longs, MAPBOX_ACCESS_KEY)
        return url

    def create_stop_location_detail(title, latitude, longitude, index, route_index):
        point = Point([longitude, latitude])
        properties = {
            "title": title,
            'icon': "campsite",
            'marker-color': '#3bb2d0',
            'marker-symbol': index,
            'route_index': route_index
        }
        feature = Feature(geometry = point, properties = properties)
        return feature

    def create_stop_locations_details():
        stop_locations = []
        for route_index, location in enumerate(ROUTE):
            if not location["is_stop_location"]:
                continue
            stop_location = create_stop_location_detail(
                location['name'],
                location['lat'],
                location['long'],
                len(stop_locations) + 1,
                route_index
            )
            stop_locations.append(stop_location)
        return stop_locations

    def get_route_data():
        # Get the route url
        route_url = create_route_url()
        # Perform a GET request to the route API
        result = requests.get(route_url)
        # Convert the return value to JSON
        data = result.json()

        geometry = data["routes"][0]["geometry"]
        route_data = Feature(geometry = geometry, properties = {})
        waypoints = data["waypoints"]
        return route_data, waypoints

    points = create_stop_locations_details()


    return render_template('home.html',title=title,points=points, user = user, ACCESS_KEY='sk.eyJ1Ijoic2FiZXJkYW5nZXIiLCJhIjoiY2pzZWJjZ3JwMTI0ZDN6bWx4bHplcWl3dyJ9.8EJHp44K185MRZExZcv_Tg')


