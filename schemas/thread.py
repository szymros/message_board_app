from ma import ma
from models.thread import ThreadModel
from marshmallow_sqlalchemy.fields import Nested
from schemas.post import PostSchema


class ThreadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ThreadModel
        load_instance = True
        include_relationships = True
        #exclude = ("id",)
    posts = Nested(PostSchema, many=True, exclude=("thread","id"))


    