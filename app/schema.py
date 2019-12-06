import graphene
from graphene import relay, Int, Field, String
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import Department, Employee


class Department(SQLAlchemyObjectType):
    class Meta:
        model = Department
        interface = (relay.Node, )

    def get_by_dept_no(info, dept_no):
        dept_query = Department.get_query(info)
        return dept_query.filter_by(dept_no=dept_no).first()


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

    departments = SQLAlchemyConnectionField(DepartmentConnection, sort=None)
    employees = SQLAlchemyConnectionField(EmployeeConnection)

    department = Field(Department, dept_no=String(required=True))

    def resolve_department(self, info, dept_no):
        return Department.get_by_dept_no(info=info, dept_no=dept_no)


schema = graphene.Schema(query=Query, types=[Department, Employee])
