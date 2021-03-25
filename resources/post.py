from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt, get_jti
import requests

from schemas.post import PostSchema
from models.post import PostModel


post_schema = PostSchema()

class PostResource(Resource):
    @classmethod
    def get(cls, id:int):
        post = PostModel.find_by_id(id)
        if post:
            return post_schema.dump(post)
        return {'msg' : 'post not found'}, 404

    @classmethod
    def delete(cls, id:int):
        post = PostModel.find_by_id(id)
        if post:
            post.delete_from_db()
            return {'msg' : 'post has been deleted'}, 200
        return {'msg' : 'post not found'}


class CreatePost(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        json = request.get_json()
        if not json["thread_id"]:
            headers = {
                "Content-Type" : "application/json",
                "Authorization" : request.headers['Authorization']
            }
            response = requests.post("http://127.0.0.1:5000/create_thread", data={}, headers=headers)
            if response.json().get('msg'):
                return response.json()
            else:
                json["thread_id"] = response.json()['id']   
        new_post = post_schema.load(json)
        if new_post:
            new_post.save_to_db()
            return post_schema.dump(new_post), 200
        return {'msg' : 'couldnt create new post'}

        