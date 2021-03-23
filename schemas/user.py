from ma import ma
from models.user import UserModel
from marshmallow_sqlalchemy.fields import Nested
from schemas.post import PostSchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        include_relationships = True
        
    #threads = Nested(ThreadSchema, many=True, exclude=("user_id",))
    posts = Nested(PostSchema, many=True, exclude=("user",))