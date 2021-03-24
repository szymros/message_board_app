from ma import ma
from marshmallow_sqlalchemy.fields import Nested

from models.post import PostModel
from schemas.user import UserSchema


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PostModel
        load_instance = True
        include_fk = True
        include_relationships = True
        load_only = ("user_id" , "thread_id")
        exclude = ("id",)
    user = Nested(UserSchema, exclude=('id','password','posts'))
    
    



