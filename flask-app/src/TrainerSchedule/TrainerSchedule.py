from flask import Blueprint, request, jsonify, make_response
import json
from src import db

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

trainer_schedule = Blueprint('TrainerSchedule', __name__)

@trainer_schedule.route('/TrainerSchedule', methods=['GET'])
def get_trainer_schedule():
    # Logic to retrieve and return all trainer schedules
    cursor = db.get_db().cursor()
    cursor.execute('select Availability, TrainerID from TrainerSchedule')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


    @trainer_schedule.route('/TrainerSchedule', methods=['POST'])
    def add_trainer_schedule():
        availability = request.form['Availability']
        trainer_id = request.form['TrainerID']
        # Insert logic
        # ...

@trainer_schedule.route('/TrainerSchedule/<int:availability_id>', methods=['PUT'])
def update_trainer_schedule(availability_id):
    availability = request.form['Availability']
    trainer_id = request.form['TrainerID']
    # Update logic
    # ...

@trainer_schedule.route('/TrainerSchedule/<int:availability_id>', methods=['DELETE'])
def delete_trainer_schedule(availability_id):
    # Delete logic
    # ...
    pass
