import urllib.request,json
import json
import requests
from geojson import Point, Feature

# from . import app
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

base_url=None
mapbox_access_key=None


def configure_request(app):
    global mapbox_access_key,base_url
    base_url = app.config['MAP_API_BASE_URL']
    mapbox_access_key = app.config['MAPBOX_ACCESS_KEY']


ROUTE = [
    {"lat": -1.2384, "long": 36.8324, "name": "Karura Forest", "is_stop_location": True},
    {"lat": 2.4382, "long": 37.6062, "name": "Marsabit National Park", "is_stop_location": True},
    {"lat": -0.536364, "long": 36.114571, "name": "Lemon Valley Farm", "is_stop_location": True},
    {"lat": 0.4120, "long": 34.1417, "name": "Rusinga Island Lounge", "is_stop_location": True},
    {"lat": -0.27456, "long": 35.97311, "name": "Egerton Castle Nakuru", "is_stop_location": True},
    {"lat": -3.30937, "long": 40.01553, "name": "Gedi Ruins", "is_stop_location": True},
    {"lat": -3.3606, "long": 39.7465, "name": "Arabuko-Sokoke", "is_stop_location": True},
    {"lat": 2.0760, "long": 36.6490, "name": "Lake Turkana National Park", "is_stop_location": True},
    {"lat": 3.17055, "long": 37.34952, "name": "Chalbi Desert Marsabit", "is_stop_location": True},
    {"lat": -3.7874, "long": 39.2572, "name": "Tsavo National Park", "is_stop_location": True}       
]



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
        'marker-color': '#6B1A74',
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

