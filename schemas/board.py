from ma import ma
from marshmallow_sqlalchemy.fields import Nested

from models.board import BoardModel
from schemas.thread import ThreadSchema

class BoardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BoardModel
        load_instance = True
        include_relationships = True
        include_fk = True
        dump_only = ('threads', )
        exclude = ('id', )
    threads = Nested(ThreadSchema, exclude=('board_id',), many=True)