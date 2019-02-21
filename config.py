# import os

# class Config:

#     MAPBOX_API_BASE_URL ='https://api.mapbox.com/directions/v5/{profile}/{coordinates}?access_token={your_access_token}'
#     # "https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/1/0/0.mvt?access_token=pk.eyJ1Ijoic2FiZXJkYW5nZXIiLCJhIjoiY2pzYnRwam1oMGRyczQ1bWxweHl4MmltdSJ9.r3PTm_k0VkCSoLtPftuwjg"
#     MAPBOX_API_KEY = os.environ.get('MAP_API_KEY')
#     MAPBOX_ACCESS_TOKEN =os.environ.get('MAPBOX_ACCESS_TOKEN')
#     SECRET_KEY = os.environ.get('SECRET_KEY')

#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     UPLOADED_PHOTOS_DEST ='app/static/photos'

#     #  email configurations
#     MAIL_SERVER = 'smtp.gmail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
#     SUBJECT_PREFIX = 'Vybe'
#     SENDER_EMAIL = 'saber.dangermouse@gmail.com'

# # simple mde  configurations
#     SIMPLEMDE_JS_IIFE = True
#     SIMPLEMDE_USE_CDN = True
#     @staticmethod
#     def init_app(app):
#         pass

# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("VYBE_DATABASE_URL")
#     pass

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("VYBE_DATABASE_URL")
#     pass

# class DevConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("VYBE_DATABASE_URL")
#     DEBUG = True

# config_options = {
#     "production":ProdConfig,
#     "development":DevConfig,
#     "testing":TestConfig
#     }

