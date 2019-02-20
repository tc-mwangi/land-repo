from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
        '''creates instances of user
        '''
    __tablename__='users'
    user_id  = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255),unique = True,nullable=False)
    email = db.Column(db.String(255),unique = True,nullable=False)
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError("Can't read")

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Places(db.Model):
    '''creates insatnces of places on the map
    '''
    __tablename__='places'
    place_id = db.Column(db.Integer,primary_key=True)
    place_name= db.Column(db.String(100),nullable=False)
    description= db.Column(db.String(300),nullable=True)
    lat = db.Column(db.Float,nullable=False)
    lng = db.Column(db.Float,nullable=False)

    def __repr__(self):
        return f' {self.place_name}, {self.description}'

class Favorites(db.Model):
    """Saved places as favorited by users."""

    __tablename__ = "favorite"

    favorite_id = db.Column(db.Integer,primary_key=True)
    landmark_id = db.Column(db.Integer, db.ForeignKey('places.place_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    # Define relationship to places
    places = db.relationship("Places", backref='saved',lazy='dynamic')
    # Define relationship to user
    user = db.relationship("User", backref='saved',lazy='dynamic')

    def __repr__(self):
        f'{self.favorite_id, self.place_id, self.user_id}'

    def __init__(self, place_id, user_id):

        self.place_id = place_id
        self.user_id = user_id
        self.favorite = []

