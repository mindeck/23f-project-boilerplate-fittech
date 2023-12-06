from flask import Blueprint, request, jsonify, make_response
import json
from src import db

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

members = Blueprint('Members', __name__)

# Get and Post all new Members
@members.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        firstName = request.form['FirstName']
        lastName = request.form['LastName']
        phoneNumber = request.form['PhoneNumber']
        email = request.form['Email']
        height = request.form['Height']
        weight = request.form['Weight']
        cursor = db.get_db().cursor()
        error = None

        if error is None:
            try:
                cursor.execute(
                    "INSERT INTO Members (FirstName, LastName, PhoneNumber, Email, Height, Weight) VALUES (?, ?, ?, ?, ?, ?)",
                    (firstName, lastName, phoneNumber, email, height, weight),
                )
                cursor.commit()
            except cursor.IntegrityError:
                error = f"Members {firstName, lastName} is already exists."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

# Get all customers from the DB
@members.route('/Members', methods=['GET'])
def get_Members():
    cursor = db.get_db().cursor()
    cursor.execute('select FirstName, LastName,\
        PhoneNumber, Email, Height, Weight from Members')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get member detail for member with particular MemberID
@members.route('/Members/<userID>', methods=['GET'])
def get_Members(MemberID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Members where MemberID = {0}'.format(MemberID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response