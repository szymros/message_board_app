from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from db import db
from ma import ma
from blocklist import BLOCKLIST

from resources.user import UserResource, CreateUser, UserLogin, UserLogout
from resources.post import PostResource, CreatePost
from resources.thread import ThreadResource, CreateThread

app = Flask(__name__)

load_dotenv()
app.config.from_object('default_config')

@app.before_first_request
def create_tables():
    db.create_all()

api = Api(app)

api.add_resource(UserResource, '/user/<string:name>')
api.add_resource(CreateUser, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

api.add_resource(PostResource, '/post/<int:id>')
api.add_resource(CreatePost, '/create_post')

api.add_resource(ThreadResource, '/thread/<int:id>')
api.add_resource(CreateThread, '/create_thread')


jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload['jti'] in BLOCKLIST


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True)