from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from flask_login import current_user,login_required

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

