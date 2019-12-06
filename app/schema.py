import graphene
from graphene import relay, Int
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import Department, Employee


class Department(SQLAlchemyObjectType):
    class Meta:
        model = Department
        interface = (relay.Node, )


class DepartmentConnection(relay.Connection):
    class Meta:
        node = Department

    total_count = Int()

    def resolve_total_count(root, info):
        return root.length


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = Employee
        interface = (relay.Node, )


class EmployeeConnection(relay.Connection):
    class Meta:
        node = Employee

    total_count = Int()

    def resolve_total_count(root, info):
        return root.length


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    departments = SQLAlchemyConnectionField(DepartmentConnection)
    employees = SQLAlchemyConnectionField(EmployeeConnection)


schema = graphene.Schema(query=Query)
