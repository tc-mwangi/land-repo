import urllib.request,json
import requests
from .models import Map

api_key = None
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MAP_API_KEY']
    base_url = app.config['MAP_API_BASE_URL']