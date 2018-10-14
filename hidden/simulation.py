import requests
from faker import Faker
import random
import os
import sqlite3 as sql

os.environ['no_proxy'] = '127.0.0.1,localhost'


fake = Faker()
deget = ["Maths", "English", "History",
         "Physics", "Chemistry", "Music",
         "Biology", "Geography", "Art",
         "Science", "Technology", "Sports",
         "Astronomy", "Computer", "Science",
         "Algebra", "Geomtry", "Calculus"]

db = sql.connect("./database/universitySystem.db")
c = db.cursor()

createTable = '''
CREATE TABLE IF NOT EXISTS Shkolla (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
password TEXT NOT NULL UNIQUE,
birthday TEXT NOT NULL,
subjects TEXT,
subjects_failed TEXT,
avarage INTEGER NOT NULL,
permission TEXT NOT NULL
);'''

c.execute(createTable)

InsertRecord = """
INSERT OR IGNORE INTO Shkolla (
id,
name,
password,
birthday,
subjects,
subjects_failed,
avarage,
permission)
VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
"""

# Admin User | User: Demo, Password: Demo
c.execute(InsertRecord, ('demo', 'demo', '2014-01-22',
                         None, None, 0, 'admin'))

db.commit()

addRecords = []
for user in range(50000):  # Simulation 50000 Users
    name = fake.name()
    password = fake.password(length=8, special_chars=False)
    birthday = fake.date_this_century()
    subjects_failed = random.sample(deget, random.randint(0, 4))
    subjects = [subject for subject in random.sample(
        deget, 12) if subject not in subjects_failed]
    avarage = random.uniform(6, 10)

    addRecords.append([name, password, str(birthday), ', '.join(subjects),
                       ', '.join(subjects_failed),
                       int(float('%.2f' % avarage) * 100), "user"])

c.executemany(InsertRecord, addRecords)

db.commit()
db.close()
