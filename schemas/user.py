from ma import ma
from models.user import UserModel

#from marshmallow_sqlalchemy.fields import Nested
#from schemas.post import PostSchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        include_relationships = True
        load_only = ("password",)
        exclude = ("id",)
    
    #posts = Nested(PostSchema, many=True, exclude=("user",))

#the comment out stuff was used to make posts a list of post objects 
#now posts is just a list of post ids
#did it becouse i wanted to display more data about user in a post
#and that required userschema to be used in postschema
#that would make definitions of these schemas required of each other
#that didnt work so i had to choose one to have a nested field