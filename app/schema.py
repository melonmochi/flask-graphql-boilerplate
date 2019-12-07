import graphene
from graphene import relay, Int, Field, String, ObjectType, List
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import Department, Employee


class ActiveSQLAlchemyObjectType(SQLAlchemyObjectType):
    class Meta:
        abstract = True

    @classmethod
    def query(cls, info):
        return cls.get_query(info)

    @classmethod
    def get_all_nodes(query):
        return query.all()

    @classmethod
    def get_node_by_id(query, id):
        return query.filter_by(id=id).first()


class Department(ActiveSQLAlchemyObjectType):
    class Meta:
        model = Department
        interface = (relay.Node, )

    def get_by_dept_no(query, dept_no):
        return query.filter_by(dept_no=dept_no).first()


class Employee(ActiveSQLAlchemyObjectType):
    class Meta:
        model = Employee
        interface = (relay.Node, )

    def get_by_emp_no(query, emp_no):
        return query.filter_by(emp_no=emp_no).first()


class EmployeeConnection(relay.Connection):
    class Meta:
        node = Employee

    total_count = Int()

    def resolve_total_count(root, info):
        return root.length


class Query(ObjectType):
    node = relay.Node.Field()
    '''Department's queries'''
    departments = List(Department)

    def resolve_departments(self, info):
        return Department.get_all_nodes(query=Department.query(info))

    department = Field(Department, dept_no=String(required=True))

    def resolve_department(self, info, dept_no):
        return Department.get_by_dept_no(query=Department.query(info),
                                         dept_no=dept_no)

    '''Employee's queries'''
    employees = SQLAlchemyConnectionField(EmployeeConnection)

    employee = Field(Employee, emp_no=String(required=True))

    def resolve_employee(self, info, emp_no):
        return Employee.get_by_emp_no(query=Employee.query(info),
                                      emp_no=emp_no)


schema = graphene.Schema(query=Query, types=[Department, Employee])
