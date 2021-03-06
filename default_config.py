import os

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_URI")
SECRET_KEY = os.environ.get("SECRET_KEY")