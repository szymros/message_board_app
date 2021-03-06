from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt, get_jti, get_jwt_identity

from schemas.post import PostSchema
from models.post import PostModel
from models.thread import ThreadModel


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
            new_thread = ThreadModel()
            new_thread.save_to_db()
            json["thread_id"] = new_thread.id
        elif not ThreadModel.find_by_id(json['thread_id']):
            return {'msg' : 'thread not found'}
        json['user_id'] = get_jwt_identity()
        new_post = post_schema.load(json)   
        if new_post:
            new_post.save_to_db()
            return post_schema.dump(new_post), 200
        return {'msg' : 'couldnt create new post'}