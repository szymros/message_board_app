from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from db import db
from ma import ma

from resources.user import UserResource, CreateUser
from resources.post import PostResource

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

@app.before_first_request
def create_tables():
    db.create_all()

api = Api(app)

api.add_resource(UserResource, '/user/<string:name>')
api.add_resource(CreateUser, '/register')
api.add_resource(PostResource, '/post')

jwt = JWTManager(app)

#db.init_app(app)
#ma.init_app(app)

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True)