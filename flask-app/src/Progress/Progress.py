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
    pass

@progress.route('/Progress', methods=['POST'])
def add_progress():
    workout_name = request.form['WorkoutName']
    sets = request.form['Sets']
    reps = request.form['Reps']
    weight = request.form['Weight']
    time = request.form['Time']
    member_id = request.form['MemberID']
    # Insert logic
    # ...

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