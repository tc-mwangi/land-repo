from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__='users'
    '''creates instances of user
    '''
    id  = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255),unique = True,nullable=False)
    email = db.Column(db.String(255),unique = True,nullable=False)
    avatar = db.Column(db.String(200), default='default.jpg')
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

class Map:
    '''creates insatnces of map
    '''

