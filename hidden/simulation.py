import requests
from faker import Faker
import random
import os
os.environ['no_proxy'] = '127.0.0.1,localhost'


fake = Faker()
deget = ["Maths", "English", "History",
         "Physics", "Chemistry", "Music",
         "Biology", "Geography", "Art",
         "Science", "Technology", "Sports",
         "Astronomy", "Computer", "Science",
         "Algebra", "Geomtry", "Calculus"]

for user in range(200):
    name = fake.name()
    password = fake.password(length=8, special_chars=False)
    birthday = fake.date_this_century()
    subjects = random.sample(deget, 12)
    subjects_failed = random.sample(deget, random.randint(0, 4))
    avarage = random.uniform(6, 10)

    args = {'name': name, 'password': password,
            'birthday': str(birthday),
            'subjects': ', '.join(
                subjects), 'subjectsFailed': ', '.join(subjects_failed),
            'avarage': int( float( '%.2f' % avarage ) * 100 ), 'permission': 'user'}
    print(args)

    with requests.post("http://127.0.0.1:5005/rest/adduser", data=args) as resp:
        print(resp.text)
