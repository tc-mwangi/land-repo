
import json
import requests
from geojson import Point, Feature
from .models import Places
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash



# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/mapbox_js')
# def mapbox_js():
#     route_data, waypoints = get_route_data()

#     stop_locations = create_stop_locations_details()

#     return render_template('mapbox_js.html', 
#         ACCESS_KEY=MAPBOX_ACCESS_KEY,
#         route_data=route_data,
#         stop_locations = stop_locations
#     )

# @app.route('/mapbox_gl')
# def mapbox_gl():
#     route_data, waypoints = get_route_data()

#     stop_locations = create_stop_locations_details()

#     # For each stop location, add the waypoint index 
#     # that we got from the route data
#     for stop_location in stop_locations:
#         waypoint_index = stop_location.properties["route_index"]
#         waypoint = waypoints[waypoint_index]
#         stop_location.properties["location_index"] = route_data['geometry']['coordinates'].index(waypoint["location"])

#     return render_template('mapbox_gl.html', 
#         ACCESS_KEY=MAPBOX_ACCESS_KEY,
#         route_data = route_data,
#         stop_locations = stop_locations
#     )
