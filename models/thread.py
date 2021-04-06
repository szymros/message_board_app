from db import db
from models.basemodel import BaseModel

class ThreadModel(BaseModel):
    __tablename__ = "thread"
    
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    posts = db.relationship('PostModel', lazy=True, backref='thread')
