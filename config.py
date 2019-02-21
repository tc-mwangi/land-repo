import os

class Config:

    # MAP_API_BASE_URL =''
    # MAP_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAPBOX_ACCESS_KEY = os.environ['MAPBOX_ACCESS_KEY']

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    #  email configurations
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # SUBJECT_PREFIX = 'Vybe'
    # SENDER_EMAIL = 'saber.dangermouse@gmail.com'

    # simple mde  configurations
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("VYBE_DATABASE_URL")
    pass

class TestConfig(Config):
    '''
    Docstring
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

config_options = {
    "production":ProdConfig,
    "development":DevConfig,
    "testing":TestConfig
}

