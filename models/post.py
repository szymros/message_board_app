from db import db
from models.basemodel import BaseModel 
from datetime import datetime

class PostModel(BaseModel):
    __tablename__ = 'post'
    contents = db.Column(db.String(300), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)