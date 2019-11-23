from flask import Blueprint, jsonify
from app.models import Departments

api = Blueprint('api', __name__)


@api.route('/departments')
def departments():
    '''List all departments'''
    departments_list = Departments.query.all()
    return jsonify([dep.serializable for dep in departments_list])
