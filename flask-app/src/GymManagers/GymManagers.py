# app/managers/routes.py
from flask import Blueprint

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import Blueprint, request, jsonify, make_response
import json
from src import db

gym_managers = Blueprint("GymManagers", __name__)

@gym_managers.route('/GymManagers', methods=['GET'])
def get_gym_managers():
    # Logic to retrieve and return all gym managers
    cursor = db.get_db().cursor()
    cursor.execute('select ManagerID, FirstName, LastName,\
        PhoneNumber, Email from GymManager')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@gym_managers.route('/GymManagers', methods=['POST'])
def add_gym_manager():
    first_name = request.form['FirstName']
    last_name = request.form['LastName']
    phone_number = request.form['PhoneNumber']
    email = request.form['Email']
    # Insert logic
    cursor = db.get_db().cursor()
        error = None

        if error is None:
            try:
                cursor.execute(
                    "INSERT INTO GymManagers (FirstName, LastName, PhoneNumber, Email) VALUES (?, ?, ?, ?,)",
                    (class_name, spots_available, start_time, membership_id),
                )
                cursor.commit()
            except cursor.IntegrityError:
                error = f"GymManagers {FirstName, LastName} already exists."
        else:
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@gym_managers.route('/GymManagers/<int:ManagerID>', methods=['PUT'])
def update_gym_manager(ManagerID):
    first_name = request.form['FirstName']
    last_name = request.form['LastName']
    phone_number = request.form['PhoneNumber']
    email = request.form['Email']
    # Update logic
    # ...
    pass

@gym_managers.route('/GymManagers/<int:ManagerID>', methods=['DELETE'])
def delete_gym_manager(ManagerID):
    # Delete logic
    # ...
    pass
