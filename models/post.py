from db import db
from datetime import datetime

class PostModel(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String(300), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id:int):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_title(cls, title:str):
        return cls.query.filter_by(title=title).first()