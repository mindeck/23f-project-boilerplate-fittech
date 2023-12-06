from flask import Blueprint, request, jsonify, make_response
import json
from src import db

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

trainer_resources = Blueprint('TrainerResources', __name__)

@trainer_resources.route('/TrainerResources', methods=['GET'])
def get_trainer_resources():
    # Logic to retrieve and return all trainer resources
    cursor = db.get_db().cursor()
    cursor.execute('select Workout, Duration,\
        Instensity, TrainerID from TrainerResources')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

@trainer_resources.route('/TrainerResources', methods=['POST'])
def add_trainer_resource():
    workout = request.form['Workout']
    duration = request.form['Duration']
    intensity = request.form['Intensity']
    trainer_id = request.form['TrainerID']
    # Insert logic
    # ...

@trainer_resources.route('/TrainerResources/<workout_name>', methods=['PUT'])
def update_trainer_resource(workout_name):
    duration = request.form['Duration']
    intensity = request.form['Intensity']
    trainer_id = request.form['TrainerID']
    # Update logic
    # ...

@trainer_resources.route('/TrainerResources/<workout_name>', methods=['DELETE'])
def delete_trainer_resource(workout_name):
    # Delete logic
    # ...
    pass
