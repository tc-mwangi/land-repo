from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db

@main.route('/')
def index():
    title = 'vYbe'
    return render_template('index.html',title=title)

