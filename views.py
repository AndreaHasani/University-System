from flask import Flask, render_template, request, session, jsonify, abort, redirect, url_for
from models import Shkolla, db
from app import application
from restApi import *


@application.route("/", methods=["GET"])
def index():
    s = session.get('status', '')
    if s:
        username = session.get('username', '')

        if s == "admin":
            users = db.session.query(Shkolla).all()
            return render_template("loginAdm.html",
                                   username=username, status=s, users=users)

        return render_template("loginUsr.html",
                               username=username, status=s)

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
        subjects = list(set([x.strip() for x in user.subjects.split(',')]))
        subjectsFailed = list(set([x.strip()
                                   for x in user.subjects_failed.split(',')]))

        return render_template("loginAdm.html", user=user,
                               subjects=subjects, subct_failed=subjectsFailed)
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
