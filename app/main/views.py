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



@main.route('/explore')
@login_required
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
@login_required
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