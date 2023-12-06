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
    pass

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