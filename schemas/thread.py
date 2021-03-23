from ma import ma
from models.thread import ThreadModel

class ThreadSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ThreadModel
        load_instance = True
    id = ma.auto_field()
    user_id = ma.auto_field()
    posts = ma.auto_field()


    