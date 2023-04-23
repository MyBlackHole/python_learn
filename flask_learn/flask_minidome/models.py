from __init__ import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(32))
    pwd = db.Column(db.String(64))
    # sex = db.Column(db.In, unique=True)


class EmpInfo(db.Model):
    __tablename__ = "empinfo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    age = db.Column(db.Integer)
    salary = db.Column(db.Float)
    operation = db.Column(db.String(128))
