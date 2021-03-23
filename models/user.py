from db import db

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    @classmethod
    def find_by_id(cls, id:int):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name:str):
        return cls.query.filter_by(username=name).first()
