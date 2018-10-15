from models import Shkolla, db, Schedule, Subjects


def getUserInfo(db, user):
    try:
        fieldSchedule = db.session.query(
            Schedule).filter_by(name=user.field).first()
        fieldSubjectsIndex = [x.split("|")[0].strip()
                              for x in fieldSchedule.subjects.split(',')]

        fieldSubjectsTime = [x.split("|")
                             for x in fieldSchedule.subjects.split(',')]

        fieldSubjects = db.session.query(Subjects.id, Subjects.name).filter(
            Subjects.id.in_(fieldSubjectsIndex)).all()

        fieldSubjectsGrade = [grade.strip().split("|")
                              for grade in user.subjects_grade.split(',')]

        dictTime = [[subject.strip(), time.strip()] for
                    subject, time in fieldSubjectsTime]
        dictGrades = [[subject, grade] for subject,
                      grade in fieldSubjectsGrade]
        dictSubjects = [[_id, subject]
                        for _id, subject in fieldSubjects]

        userInfo = [[_id, time, subject, grade] for _id,
                    subject in dictSubjects for b,
                    grade in dictGrades if str(_id) == b for c,
                    time in dictTime if str(_id) == c]

        return userInfo

    except Exception as e:
        raise e
        return 0
