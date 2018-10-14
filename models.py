from app import application
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(application)


class Shkolla(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    birthday = db.Column(db.String)
    field = db.Column(db.String)
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



class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    teacher = db.Column(db.String)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    subjects = db.Column(db.String)
    head_teacher = db.Column(db.String)
    monday = db.Column(db.String)
    tuesday = db.Column(db.String)
    wednesday = db.Column(db.String)
    thursday = db.Column(db.String)
    friday = db.Column(db.String)
