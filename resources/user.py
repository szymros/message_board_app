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

    def delete(cls, id:int):
        user = UserModel.find_by_id(id)
        if user:
            user.delete_from_db()
            return {'msg' : 'user deleted form db'}, 200
        return {'msg': 'user not found'}, 404

class CreateUser(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        if UserModel.find_by_name(data['username']):
            return {'msg' : 'user already exists'}, 403
        new_user = user_schema.load(data)
        if new_user:
            new_user.save_to_db()
            return user_schema.dump(new_user), 200
        return {'msg' : 'couldnt create new user'}
