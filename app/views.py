from flask import Blueprint, jsonify
from app.models import Departments, Employees

api = Blueprint('api', __name__)


@api.route('/departments')
def departments():
    '''List all departments'''
    departments_list = Departments.query.all()
    return jsonify([dep.serializable for dep in departments_list])


@api.route('/employees')
def employees():
    '''List all employees'''
    employees_list = Employees.query.all()
    return jsonify([emp.serializable for emp in employees_list])
