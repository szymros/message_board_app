from ma import ma
from models.user import UserModel

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel
        load_instance = True
    id = ma.auto_field()
    username = ma.auto_field()
    password = ma.auto_field()