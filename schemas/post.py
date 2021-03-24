from ma import ma
from models.post import PostModel
from schemas.user import UserSchema
from marshmallow_sqlalchemy.fields import Nested



class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PostModel
        load_instance = True
        include_relationships = True
        exclude = ("id",)
    user = Nested(UserSchema, many=False, exclude=("posts","password"))




