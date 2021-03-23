from flask_restful import Resource
from flask import request
from schemas.post import PostSchema
from models.post import PostModel

post_schema = PostSchema()

class PostResource(Resource):
    @classmethod
    def get(cls, title:str):
        post = PostModel.find_by_title(title)
        if post:
            return post_schema.dump(post)
        return {'msg' : 'post not found'}, 404

class CreatePost(Resource):
    @classmethod
    def post(cls):
        json = request.get_json()
        new_post = post_schema.load(json)
        if new_post:
            new_post.save_to_db()
            return post_schema.dump(new_post), 200