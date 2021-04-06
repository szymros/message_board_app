from models.basemodel import BaseModel
from db import db

class BoardModel(BaseModel):
    __tablename__ = 'board'
    board_name = db.Column(db.String(40), unique=True, nullable=False)
    
    threads = db.relationship('ThreadModel', lazy=True, backref='board')

    @classmethod
    def find_by_name(cls, name:str):
        return cls.query.filter_by(board_name=name).first()