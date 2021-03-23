from db import db

class ThreadModel(db.Model):
    __tablename__ = "thread"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    posts = db.relationship('PostModel', lazy=True, backref='thread')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def find_by_id(cls, id:int):
        return cls.query.filter_by(id=id).first()