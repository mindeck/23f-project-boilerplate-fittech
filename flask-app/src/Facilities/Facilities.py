# app/facilities/routes.py
from flask import(Blueprint, request)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import Blueprint, request, jsonify, make_response
import json
from src import db

facilities = Blueprint("Facilities", __name__)

@facilities.route('/Facilities', methods=['GET'])
def get_facilities():
    # Logic to retrieve and return all facilities
    cursor = facilities.get_db().cursor()
    cursor.execute('select EquipmentID, PurchaseDate,\
        LastMaintenanceDate, Name, Manufacturer, Condition,\
                    ManagerID from Facilities')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@facilities.route('/Facilities', methods=['POST'])
def add_facility():
    purchase_date = request.form['PurchaseDate']
    last_maintenance_date = request.form['LastMaintenanceDate']
    name = request.form['Name']
    manufacturer = request.form['Manufacturer']
    condition = request.form['Condition']
    manager_id = request.form['ManagerID']
    # Insert logic
    cursor = db.get_db().cursor()
        error = None

        if error is None:
            try:
                cursor.execute(
                    "INSERT INTO Facilities (PurchaseDate, LastMaintenanceDate, Name, Manufacturer, Condition, ManagerID) VALUES (?, ?, ?, ?, ?, ?)",
                    (class_name, spots_available, start_time, membership_id),
                )
                cursor.commit()
            except cursor.IntegrityError:
                error = f"Facilities {Name, Manufacturer} already exists."
        else:
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@facilities.route('/Facilities/<int:EquipmentID>', methods=['PUT'])
def update_facility(EquipmentID):
    purchase_date = request.form['PurchaseDate']
    last_maintenance_date = request.form['LastMaintenanceDate']
    name = request.form['Name']
    manufacturer = request.form['Manufacturer']
    condition = request.form['Condition']
    manager_id = request.form['ManagerID']
    # Update logic
    # ...
    pass

@facilities.route('/Facilities/<int:EquipmentID>', methods=['DELETE'])
def delete_facility(EquipmentID):
    # Delete logic
    # ...
    return 'deleted'
