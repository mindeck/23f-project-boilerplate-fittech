from flask import Blueprint, request, jsonify, make_response
import json
from src import db

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

workout_plan = Blueprint('WorkoutPlan', __name__)

@workout_plan.route('/WorkoutPlan', methods=['GET'])
def get_workout_plans():
    # Logic to retrieve and return all workout plans
    cursor = db.get_db().cursor()
    cursor.execute('select Goals, WorkoutType,\
        MemberID from WorkoutPlan')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@workout_plan.route('/WorkoutPlan', methods=['POST'])
def add_workout_plan():
    goals = request.form['Goals']
    workout_type = request.form['WorkoutType']
    member_id = request.form['MemberID']
    # Insert logic
    # ...

@workout_plan.route('/WorkoutPlan/<int:plan_id>', methods=['PUT'])
def update_workout_plan(plan_id):
    goals = request.form['Goals']
    workout_type = request.form['WorkoutType']
    member_id = request.form['MemberID']
    # Update logic
    # ...

@workout_plan.route('/WorkoutPlan/<int:plan_id>', methods=['DELETE'])
def delete_workout_plan(plan_id):
    # Delete logic
    # ...
    pass
