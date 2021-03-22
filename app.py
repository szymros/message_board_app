from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from db import db
from ma import ma

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_RUI")
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

api = Api(app)
jwt = JWTManager(app)

db.init_app(app)
ma.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)