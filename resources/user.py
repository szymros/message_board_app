from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from passlib.hash import pbkdf2_sha256

from db import db
from blocklist import BLOCKLIST

from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()
custom_hash = pbkdf2_sha256.using(rounds=30000,salt_size=16)
                                #(rounds, salt, salt_size) 
                                # rounds = how many times is hashed
                                # salt = added characters and salt_size = how many of these characters

class UserResource(Resource):
    @classmethod
    @jwt_required()
    def get(cls, name:str):
        user = UserModel.find_by_name(name)
        if user:
            return user_schema.dump(user)
        else:
            return {'msg' : 'user not found'}, 404

    @jwt_required()
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
        hashed = pbkdf2_sha256.hash(data['password'])
        data['password'] = hashed
        new_user = user_schema.load(data)
        if new_user:
            new_user.save_to_db()
            return user_schema.dump(new_user), 200
        return {'msg' : 'couldnt create new user'}
        
        
class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        user = UserModel.find_by_name(data['username'])
        #todo add salt to hash
        if user and pbkdf2_sha256.verify(data['password'], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            return{'access_token' : access_token}, 200
        return {'msg' : 'incorrect credentials'}, 403

class UserLogout(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        jti = get_jwt()['jti']
        BLOCKLIST.add(jti)
        return {'msg' : 'user logged out'}