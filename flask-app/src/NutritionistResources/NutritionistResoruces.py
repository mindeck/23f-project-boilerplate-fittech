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
    # Logic to retrieve and return all trainer resources
    pass

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
