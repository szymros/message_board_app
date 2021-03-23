from db import db
from datetime import datetime

class PostModel(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    contents = db.Column(db.String(300), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()