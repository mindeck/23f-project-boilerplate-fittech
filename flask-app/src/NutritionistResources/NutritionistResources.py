from flask import Blueprint, request, jsonify, make_response
import json
from src import db

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

nutritionist_resources = Blueprint('NutritionistResources', __name__)

@nutritionist_resources.route('/NutritionistResources', methods=['GET'])
def get_nutritionist_resources():
    # Logic to retrieve and return all nutritionist resources
    cursor = db.get_db().cursor()
    cursor.execute('select Food, Calories,\
        Nutrients, Protein, Carbs, NutritionistID from NutritionistResources')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@nutritionist_resources.route('/NutritionistResources', methods=['POST'])
def add_nutritionist_resources():
    food = request.form['Food']
    calories = request.form['Calories']
    nutrients = request.form['Nutrients']
    protein = request.form['Protein']
    carbs = request.form['Carbs']
    # Insert logic
    # ...

@nutritionist_resources.route('/NutritionistResources/<workout_name>', methods=['PUT'])
def update_nutritionist_resources(workout_name):
    food = request.form['Food']
    calories = request.form['Calories']
    nutrients = request.form['Nutrients']
    protein = request.form['Protein']
    carbs = request.form['Carbs']
    # Update logic
    # ...

@nutritionist_resources.route('/NutritionistResources/<workout_name>', methods=['DELETE'])
def delete_nutritionist_resources(workout_name):
    food = request.form['Food']
    calories = request.form['Calories']
    nutrients = request.form['Nutrients']
    protein = request.form['Protein']
    carbs = request.form['Carbs']
    # Delete logic
    # ...
