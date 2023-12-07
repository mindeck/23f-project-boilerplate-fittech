from flask import Blueprint, request, jsonify, make_response
import json
from src import db

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

classes = Blueprint('Classes', __name__)

@classes.route('/Classes', methods=['GET'])
def get_classes():
    # Logic to retrieve and return all classes
    cursor = db.get_db().cursor()
    cursor.execute('select ClassID, SpotsAvailable,\
        StartTime, MemberID from Classes')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@classes.route('/Classes', methods=['POST'])
def add_class():
    class_name = request.form['ClassName']
    spots_available = request.form['SpotsAvailable']
    start_time = request.form['StartTime']
    membership_id = request.form['MemberID']
    cursor = db.get_db().cursor()
        error = None

        if error is None:
            try:
                cursor.execute(
                    "INSERT INTO Classes (ClassName, SpotsAvailable, StartTime, MemberID) VALUES (?, ?, ?, ?,)",
                    (class_name, spots_available, start_time, membership_id),
                )
                cursor.commit()
            except cursor.IntegrityError:
                error = f"Classes {class_name, start_time} already exists."
        else:
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@classes.route('/Classes/<int:class_id>', methods=['PUT'])
def update_class(class_id):
    class_name = request.form['ClassName']
    spots_available = request.form['SpotsAvailable']
    start_time = request.form['StartTime']
    membership_id = request.form['MemberID']
    
