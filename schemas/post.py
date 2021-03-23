from ma import ma
from models.post import PostModel


class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PostModel
        load_instance = True
    id = ma.auto_field()
    title = ma.auto_field()
    contents = ma.auto_field()
    date = ma.auto_field()
    user_id = ma.auto_field()
    thread_id = ma.auto_field()



