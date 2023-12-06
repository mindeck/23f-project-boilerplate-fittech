from flask import Blueprint, request, jsonify, make_response
import json
from src import db

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

nutrition_plan = Blueprint('NutrionPlan', __name__)

@nutrition_plan.route('/NutritionPlan', methods=['GET'])
def get_nutrition_plans():
    # Logic to retrieve and return all nutrition plans
    cursor = db.get_db().cursor()
    cursor.execute('select Goals, DietRestrictions, MealPlan, DietType,\
                    MemberID from NutritionPlan')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@nutrition_plan.route('/NutritionPlan', methods=['POST'])
def add_nutrition_plan():
    goals = request.form['Goals']
    diet_restrictions = request.form['DietRestrictions']
    meal_plan = request.form['MealPlan']
    diet_type = request.form['DietType']
    member_id = request.form['MemberID']
    # Insert logic
    # ...

@nutrition_plan.route('/NutritionPlan/<int:plan_id>', methods=['PUT'])
def update_nutrition_plan(plan_id):
    goals = request.form['Goals']
    diet_restrictions = request.form['DietRestrictions']
    meal_plan = request.form['MealPlan']
    diet_type = request.form['DietType']
    member_id = request.form['MemberID']
    # Update logic
    # ...

@nutrition_plan.route('/NutritionPlan/<int:plan_id>', methods=['DELETE'])
def delete_nutrition_plan(plan_id):
    # Delete logic
    # ...
    pass
