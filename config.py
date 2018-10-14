import datetime
from os import urandom

SQLALCHEMY_DATABASE_URI = 'sqlite:////home/strixx/projects/websites/University-System/hidden/database/universitySystem.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = urandom(24)
PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)
