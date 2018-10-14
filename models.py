from app import application
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(application)


class Shkolla(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    birthday = db.Column(db.String)
    subjects = db.Column(db.String)
    subjects_failed = db.Column(db.String)
    avarage = db.Column(db.Integer)
    permission = db.Column(db.String)

    def __init__(self, name, password, birthday, subjects, subjects_failed, avarage, permission):
        self.name = name
        self.password = password
        self.birthday = birthday
        self.subjects = subjects
        self.subjects_failed = subjects_failed
        self.avarage = avarage
        self.permission = permission
