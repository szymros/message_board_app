from db import db

class UserModel(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    
    posts = db.relationship('PostModel', lazy=True, backref='user')
    #backref is just a short cut to not put another db.relationship in postmodel
    #lazy is a loader option of relationships im not sure how to it really wokrs
    #todo read docs about lazy
    

    @classmethod
    def find_by_id(cls, id:int):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name:str):
        return cls.query.filter_by(username=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.add(self)
        db.session.commit()
