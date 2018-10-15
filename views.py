from flask import Flask, render_template, request, session, jsonify, abort, redirect, url_for
from sqlalchemy import or_
from models import Shkolla, db, Schedule, Subjects
from app import application
from functions import getUserInfo
from restApi import *
from collections import defaultdict


@application.route("/", methods=["GET"])
def index():
    s = session.get('status', '')
    if s:
        username = session.get('username', '')

        if s == "admin":
            users = db.session.query(Shkolla).all()
            # fieldSubjects = db.session.query(Schedule.subjects).filter_by(u
            # subjects = db.session.query(Subjects).filter([Shkolla.id == v for v in Shkolla.)
            return render_template("loginAdm.html",
                                   username=username, status=s, users=users)
        else:
            user = db.session.query(Shkolla).filter_by(name=username).first()
            userInfo = getUserInfo(db, user)

            if not userInfo:
                return redirect(url_for('index'))
            else:
                return render_template("loginUsr.html",
                                       username=user, status=s,
                                       subjects=sorted(userInfo,
                                                       key=lambda x: x[1]))

    return render_template("index.html")


@application.route("/statistika", methods=["GET"])
def statistika():
    if session.get('status', '') == 'admin':
        return render_template("loginAdm.html")
    else:
        return redirect(url_for('index'))


@application.route("/addusers", methods=["GET"])
def addUsers():
    if session.get('status', '') == 'admin':
        return render_template("loginAdm.html")
    else:
        return redirect(url_for('index'))


@application.route("/edituser/<int:page_id>", methods=["GET"])
def editUser(page_id):
    if session.get('status', '') == 'admin':
        user = db.session.query(Shkolla).filter_by(id=page_id).first()
        fieldSchedule = db.session.query(
            Schedule).filter_by(name=user.field).first()
        fieldSubjectsIndex = [x.split("|")[0].strip()
                              for x in fieldSchedule.subjects.split(',')]
        fieldSubjects = db.session.query(
            Subjects).filter(Subjects.id.in_(fieldSubjectsIndex)).all()

        subjectsFailed = db.session.query(
            Subjects).filter(Subjects.id.in_(user.subjects_grade)).all()

        return render_template("loginAdm.html", user=user, subjects=fieldSubjects)
    else:
        return redirect(url_for('index'))

# Api Endpints
###
###


# @application.route("/rest/subject_failed", methods=["POST"])
# def subjects_failed():
#     uname = request.form.get("uname", "", str)
#     dlindja = request.form.get("dlindja", "", str)
#     deget = request.form.get("deget_dropdown", "", str)
#     mesatarja = request.form.get("mesatarja", "", str)

#     result = uname, dlindja, deget, mesatarja
#     return jsonify(result=result)
