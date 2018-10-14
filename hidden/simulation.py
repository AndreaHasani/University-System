import requests
from faker import Faker
import random
import os
import sqlite3 as sql

os.environ['no_proxy'] = '127.0.0.1,localhost'


def fakeTime():
    """ Generate fake time"""

    hours = random.randint(7, 18)
    minutes = ['00', 15, 30, 45]

    return "%s:%s" % (hours, random.choice(minutes))


def CreateTable(c, db):
    ctSchool = '''
    CREATE TABLE IF NOT EXISTS Shkolla (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT NOT NULL UNIQUE,
    birthday TEXT NOT NULL,
    field TEXT NOT NULL,
    subjects_failed TEXT,
    avarage INTEGER NOT NULL,
    permission TEXT NOT NULL
    );'''

    ctSubjects = '''
    CREATE TABLE IF NOT EXISTS Subjects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher TEXT NOT NULL
    );'''

    ctSchedule = '''
    CREATE TABLE IF NOT EXISTS Schedule (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    subjects TEXT NOT NULL,
    head_teacher TEXT NOT NULL,
    monday TEXT NOT NULL,
    tuesday TEXT NOT NULL,
    wednesday TEXT NOT NULL,
    thursday TEXT NOT NULL,
    friday TEXT NOT NULL
    );'''

    c.execute(ctSchool)
    c.execute(ctSchedule)
    c.execute(ctSubjects)

    # Admin User | User: Demo, Password: Demo


def generateDummyRecords(c, studyField, subjects):

    ShkollaRecords = [
        ['demo', 'demo', '2014-01-22',
         '', '', 0, 'admin'],
        ['student', 'student', '2014-02-22',
         '', '', 0, 'student'],
    ]
    for user in range(500):  # Simulation 2000 Users
        name = fake.name()
        password = fake.password(length=8, special_chars=False)
        birthday = fake.date_this_century()
        field = random.choice(studyField)
        subjects_failed = [str(subjects.index(s)) for s in random.sample(
            subjects, random.randint(0, 4))]
        avarage = random.uniform(6, 10)

        ShkollaRecords.append([name, password, str(birthday), field,
                               ', '.join(subjects_failed),
                               int(float('%.2f' % avarage) * 100), "student"])

    SchedulerRecords = []
    for field in studyField:
        fieldSubjects = ["%s|%s" % (subjects.index(subject), fakeTime())
                         for subject in random.sample(subjects,
                                                      random.randint(8, 12))]
        head_teacher = fake.name()
        monday = random.sample(fieldSubjects, random.randint(3, 6))
        tuesday = random.sample(fieldSubjects, random.randint(3, 4))
        wednesday = random.sample(fieldSubjects, random.randint(2, 4))
        thursday = random.sample(fieldSubjects, random.randint(3, 6))
        friday = random.sample(fieldSubjects, random.randint(2, 4))

        weekday = [', '.join(day) for day in [
            monday, tuesday, wednesday, thursday, friday]]

        SchedulerRecords.append(
            [field, ', '.join(fieldSubjects), head_teacher] + weekday)

    SubjectsRecords = []
    for subject in subjects:
        teacher = fake.name()

        SubjectsRecords.append([subject, teacher])

    return ShkollaRecords, SchedulerRecords, SubjectsRecords


def insertRecords(c, Shkolla, Scheduler, Subjects):
    InsertShkolla = """
    INSERT OR IGNORE INTO Shkolla (
    id,
    name,
    password,
    birthday,
    field,
    subjects_failed,
    avarage,
    permission)
    VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
    """

    InsertSubjects = """
    INSERT OR IGNORE INTO Subjects (
    id,
    name,
    teacher)
    VALUES (NULL, ?, ?)
    """

    InsertSchedule = """
    INSERT OR IGNORE INTO Schedule (
    id,
    name,
    subjects,
    head_teacher,
    monday,
    tuesday,
    wednesday,
    thursday,
    friday)
    VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    c.executemany(InsertShkolla, Shkolla)
    c.executemany(InsertSchedule, Scheduler)
    c.executemany(InsertSubjects, Subjects)


if __name__ == "__main__":

    fake = Faker()
    studyField = ["Civil Engineering", "Chemical Engineering",
                  "Communication", "Environmental Engineering",
                  "Government", "History of Art", "Landscape Architecture"]

    subjects = ["Maths", "English", "History",
                "Physics", "Chemistry", "Music",
                "Biology", "Geography", "Art",
                "Science", "Technology", "Sports",
                "Astronomy", "Computer", "Science",
                "Algebra", "Geomtry", "Calculus"]

    try:
        db = sql.connect("./database/universitySystem.db")
    except Exception as e:
        os.makedirs("database")
        db = sql.connect("./database/universitySystem.db")
    c = db.cursor()

    CreateTable(c, db)
    shkolla, schedule, subjects = generateDummyRecords(c, studyField, subjects)
    insertRecords(c, shkolla, schedule, subjects)

    db.commit()
    db.close()
