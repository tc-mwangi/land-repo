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
    __tablename__= 'users'

    id  = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255),unique = True,nullable=False)
    email = db.Column(db.String(255),unique = True,nullable=False)
    avatar = db.Column(db.String(200), default='default.jpg')
    pass_secure = db.Column(db.String(255))
    favorites = db.relationship('Favorites',backref = 'favorite',lazy ="dynamic")


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

    id = db.Column(db.Integer,primary_key=True)
    place_name= db.Column(db.String(100),nullable=False)
    region = db.Column(db.String(100),nullable=False)
    description= db.Column(db.String(300),nullable=True)
    lat = db.Column(db.Float,nullable=False)
    lng = db.Column(db.Float,nullable=False)
    image = db.Column(db.String, default='default.jpg')
    reviews = db.relationship('Review',backref = 'reviews',lazy ="dynamic")
    fav = db.relationship('Favorites',backref = 'favorites',lazy ="dynamic")

    def save_place(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f' {self.place_name}, {self.description}'

class Favorites(db.Model):
    """Saved places as favorited by users."""

    __tablename__ = "favorite"

    id = db.Column(db.Integer,primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey("places.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


    def save_favorite(self):
        db.session.add(self)
        db.session.commit()

class Review(db.Model):
	__tablename__ = 'reviews'
    
	id = db.Column(db.Integer, primary_key=True)
	name= db.Column(db.String(255))
	review = db.Column(db.Text)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	place_id = db.Column(db.Integer, db.ForeignKey("places.id"), nullable=False)



	def save_review(self):
		db.session.add(self)
		db.session.commit()