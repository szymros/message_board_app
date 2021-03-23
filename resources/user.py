from flask_restful import Resource
from models.user import UserModel
from schemas.user import UserSchema
from flask import request
from db import db

user_schema = UserSchema()

class UserResource(Resource):
    @classmethod
    def get(cls, name:str):
        user = UserModel.find_by_name(name)
        if user:
            return user_schema.dump(user)
        else:
            return {'msg' : 'user not found'}, 404



class CreateUser(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        if UserModel.find_by_name(data['username']):
            return {'msg' : 'user already exists'}
        new_user = user_schema.load(data)
        if new_user:
            db.session.add(new_user)
            db.session.commit()
            return user_schema.dump(new_user), 200
