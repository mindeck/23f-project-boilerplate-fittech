from flask import Blueprint, request, jsonify, make_response
import json
from src import db

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

progress = Blueprint('Progress', __name__)

@progress.route('/Progress', methods=['GET'])
def get_progress():
    # Logic to retrieve and return all progress records
    cursor = db.get_db().cursor()
    cursor.execute('select WorkoutName, Sets, Reps, Weights, Time, MemberID from Progress')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@progress.route('/Progress', methods=['POST'])
def add_progress():
    workout_name = request.form['WorkoutName']
    sets = request.form['Sets']
    reps = request.form['Reps']
    weight = request.form['Weight']
    time = request.form['Time']
    member_id = request.form['MemberID']
    # Insert logic
    cursor = db.get_db().cursor()
        error = None

        if error is None:
            try:
                cursor.execute(
                    "INSERT INTO Progress (WorkoutName, Sets, Reps, Weight, Time, MemberID) VALUES (?, ?, ?, ?, ?, ?,)",
                    (class_name, spots_available, start_time, membership_id),
                )
                cursor.commit()
            except cursor.IntegrityError:
                error = f"Progress {workout_name,} already exists."
        else:
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@progress.route('/Progress/<int:progress_id>', methods=['PUT'])
def update_progress(progress_id):
    workout_name = request.form['WorkoutName']
    sets = request.form['Sets']
    reps = request.form['Reps']
    weight = request.form['Weight']
    time = request.form['Time']
    member_id = request.form['MemberID']
    # Update logic
    # ...

@progress.route('/Progress/<int:progress_id>', methods=['DELETE'])
def delete_progress(progress_id):
    # Delete logic
    # ...
    pass
