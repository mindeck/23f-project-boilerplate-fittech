# app/trainers/routes.py
from flask import Blueprint, request, jsonify, make_response
import json
from src import db

nutritionists = Blueprint("trainers", __name__)


@nutritionists.route('/Nutritionists', methods=['GET'])
def get_nutritionists():
    # Logic to retrieve and return all nutritionists
    cursor = db.get_db().cursor()
    cursor.execute('select NutritionistID, FirstName,\
        LastName, PhoneNumber, Email, ManagerID from Nutritionists')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@nutritionists.route('/Nutritionists', methods=['POST'])
def add_nutritionist():
    first_name = request.form['FirstName']
    last_name = request.form['LastName']
    phone_number = request.form['PhoneNumber']
    email = request.form['Email']
    manager_id = request.form['ManagerID']
    # Insert logic
    # ...

@nutritionists.route('/Nutritionists/<int:nutritionist_id>', methods=['PUT'])
def update_nutritionist(nutritionist_id):
    first_name = request.form['FirstName']
    last_name = request.form['LastName']
    phone_number = request.form['PhoneNumber']
    email = request.form['Email']
    manager_id = request.form['ManagerID']
    # Update logic
    # ...

@nutritionists.route('/Nutritionists/<int:nutritionist_id>', methods=['DELETE'])
def delete_nutritionist(nutritionist_id):
    # Delete logic
    # ...
    pass
