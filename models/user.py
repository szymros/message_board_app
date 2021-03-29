from db import db
from models.basemodel import BaseModel

class UserModel(BaseModel):
    __tablename__= 'user'
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    
    posts = db.relationship('PostModel', lazy=True, backref='user')
    #backref is just a short cut to not put another db.relationship in postmodel
    #lazy is a loader option of relationships im not sure how to it really wokrs
    #todo read docs about lazy
    
    @classmethod
    def find_by_name(cls, name:str):
        return cls.query.filter_by(username=name).first()