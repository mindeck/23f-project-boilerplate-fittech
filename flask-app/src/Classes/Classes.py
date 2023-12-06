from flask import Blueprint, request, jsonify, make_response
import json
from src import db

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

classes = Blueprint('Classes', __name__)

@classes.route('/Classes', methods=['GET'])
def get_classes():
    # Logic to retrieve and return all classes
    pass

@classes.route('/Classes', methods=['POST'])
def add_class():
    class_name = request.form['ClassName']
    spots_available = request.form['SpotsAvailable']
    start_time = request.form['StartTime']
    membership_id = request.form['MembershipID']
    # Insert logic
    # ...

@classes.route('/Classes/<int:class_id>', methods=['PUT'])
def update_class(class_id):
    class_name = request.form['ClassName']
    spots_available = request.form['SpotsAvailable']
    start_time = request.form['StartTime']
    membership_id = request.form['MembershipID']
    #
