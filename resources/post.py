from flask_restful import Resource
from flask import request
from schemas.post import PostSchema

post_schema = PostSchema()

class PostResource(Resource):
    @classmethod
    def post(cls):
        json = request.get_json()
        new_post = post_schema.load(json)
        if new_post:
            new_post.save_to_db()
            return post_schema.dump(new_post)