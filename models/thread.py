from db import db
from models.basemodel import BaseModel

class ThreadModel(BaseModel):
    __tablename__ = "thread"
    
    posts = db.relationship('PostModel', lazy=True, backref='thread')
