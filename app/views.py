from flask import Blueprint, jsonify
from flask_graphql import GraphQLView
from app.models import Department, Employee
from app.schema import schema

api = Blueprint('api', __name__)

api.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    ))


@api.route('/departments')
def departments():
    '''List all departments'''
    departments_list = Department.query.all()
    return jsonify([dep.serializable for dep in departments_list])


@api.route('/employees')
def employees():
    '''List all employees'''
    employees_list = Employee.query.all()
    return jsonify([emp.serializable for emp in employees_list])
