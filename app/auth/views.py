from . import auth
from flask import render_template,redirect,url_for, flash,request
from ..models import User,Places
from .forms import LoginForm,RegistrationForm,PlaceForm
from .. import db
from flask_login import login_user,logout_user,login_required

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/register',methods = ["GET","POST"])
def register():

    login_form = LoginForm()
    form = RegistrationForm()

    # Sign up validation
    if form.validate_on_submit():
        user = User(name = form.name.data, email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.register"))
    
    # Log in validation
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.profile'))

        flash('Invalid username or Password')
        
    return render_template('auth/register.html',registration_form = form,login_form = login_form)

@auth.route('/add_location',methods = ["GET","POST"])
def add_location():

    place_form = PlaceForm()

    if place_form.validate_on_submit():
        place = Places(place_name = place_form.place.data, region = place_form.region.data, lat = place_form.lat.data, lng = place_form.lng.data)

        if place is not None:
            place.save_place()

            return redirect(url_for("auth.add_location"))
    return render_template('auth/add-locale.html', place_form=place_form)