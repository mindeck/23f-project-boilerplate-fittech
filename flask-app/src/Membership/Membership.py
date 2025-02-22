from flask import Blueprint, request, jsonify, make_response
import json
from src import db

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

membership = Blueprint('Membership', __name__)

@membership.route('/Membership', methods=['GET'])
def get_memberships():
    # Logic to retrieve and return all memberships
    cursor = db.get_db().cursor()
    cursor.execute('select MembershipID, StartDate,\
        EndDate, CreditCard, MemberID from MembershipID')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@membership.route('/Membership', methods=['POST'])
def add_membership():
    start_date = request.form['StartDate']
    end_date = request.form['EndDate']
    credit_card = request.form['CreditCard']
    member_id = request.form['MemberID']
    # Insert logic
    cursor = db.get_db().cursor()
        error = None

        if error is None:
            try:
                cursor.execute(
                    "INSERT INTO Membership (StartDate, End, CreditCard, MemberID) VALUES (?, ?, ?, ?,)",
                    (start_date, end_date, credit_card, membership_id),
                )
                cursor.commit()
            except cursor.IntegrityError:
                error = f"Membership {member_id,} already exists."
        else:
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@membership.route('/Membership/<int:membership_id>', methods=['PUT'])
def update_membership(membership_id):
    start_date = request.form['StartDate']
    end_date = request.form['EndDate']
    credit_card = request.form['CreditCard']
    member_id = request.form['MemberID']
    # Update logic
    # ...

@membership.route('/Membership/<int:membership_id>', methods=['DELETE'])
def delete_membership(membership_id):
    # Delete logic
    # ...
    pass
