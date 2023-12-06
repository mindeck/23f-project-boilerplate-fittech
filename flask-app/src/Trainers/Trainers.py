# app/trainers/routes.py
from flask import Blueprint, request, jsonify, make_response
import json
from src import db

trainers_bp = Blueprint("trainers", __name__)

@trainers_bp.route('/trainers', methods=['GET'])
def get_trainers():
    # Get all gym trainers
    cursor = db.get_db().cursor()
    cursor.execute('select TrainerID, PhoneNumber,\
        LastName, FirstName, Email, ManagerID from Trainers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@trainers_bp.route('/trainers', methods=['POST'])
def add_trainer():
    # Add a new gym trainer
    pass

@trainers_bp.route('/trainers/<int:trainer_id>', methods=['GET'])
def get_trainer(trainer_id):
    # Get details of a specific gym trainer
    cursor = db.get_db().cursor()
    cursor.execute('select * from Trainers where trainer_id = {0}'.format(trainer_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@trainers_bp.route('/trainers/<int:trainer_id>', methods=['PUT'])
def update_trainer(trainer_id):
    # Update details of a specific gym trainer
    pass

@trainers_bp.route('/trainers/<int:trainer_id>', methods=['DELETE'])
def delete_trainer(trainer_id):
    # Delete a specific gym trainer
    pass
