from flask import Flask, render_template, request, session, jsonify, abort, redirect, url_for
from models import Shkolla, db
from app import application


@application.route("/rest/login", methods=["POST"])
def login():
    username = request.form.get("username", "", str)
    password = request.form.get("password", "", str)

    user = db.session.query(Shkolla).filter_by(
        name=username, password=password).first()

    if user:
        session['username'] = user.name
        session['status'] = user.permission
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@application.route("/rest/logout", methods=["GET"])
def logout():
    session.clear()

    # session['username'] = "username"
    # session['status'] = "user"

    return redirect(url_for('index'))


@application.route("/rest/adm_edit", methods=["POST"])
def recordEdit():

    if session.get('status', '') != 'admin':
        return redirect(url_for('index'))

    first = request.form.get("first", None, str).split(',')
    second = request.form.get("second", None, str)
    third = request.form.get("third", None, str)
    __id = request.form.get("id", None, str)

    user = Shkolla.query.filter_by(
        id=__id).first()

    try:
        user.name = first[0]
        user.password = first[1]
        user.birthday = first[2]
        user.avarage = int(float(first[3]) * 100)
        user.permission = first[4]

        user.subjects = second
        user.subjects_failed = third

        db.session.commit()
    except Exception as e:
        raise e
        return jsonify(result="Error", code=500)

    return jsonify(result="Success", code=200)


@application.route("/rest/adduser", methods=["POST"])
def recordAdd():

    if session.get('status', '') == 'admin':
        name = request.form.get("name", None, str)
        password = request.form.get("password", None, str)
        birthday = request.form.get("birthday", None, str)
        subjects = request.form.get("subjects", None, str)
        subjectsFailed = request.form.get("subjectsFailed", None, str)
        avarage = request.form.get("avarage", None, int)
        permission = request.form.get("permission", None, str)
        variables = [name, password,
                     birthday, subjects,
                     subjectsFailed, avarage, permission]
        print(variables)

        if all(v is not None for v in variables):
            try:
                db.session.add(Shkolla(name, password, birthday,
                                       subjects, subjectsFailed,
                                       avarage, permission))
                db.session.commit()
                resp = "Success"
            except Exception as e:
                print(e)
                resp = "Error"
        else:
            resp = "Error"

        return jsonify(response=resp)
    else:
        abort(404)
