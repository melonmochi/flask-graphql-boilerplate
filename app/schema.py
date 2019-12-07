import graphene
from graphene import relay, Int, Field, String, ObjectType, List
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from sqlalchemy.sql.expression import func
from app.models import DepartmentModel, EmployeeModel, DeptManagerModel


class ActiveSQLAlchemyObjectType(SQLAlchemyObjectType):
    class Meta:
        abstract = True

    @classmethod
    def query(cls, info):
        return cls.get_query(info)


class Department(ActiveSQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interface = (relay.Node, )

    def get_by_dept_no(query, dept_no):
        return query.filter_by(dept_no=dept_no).first()

    def filter_by_q(query, q):
        return query.filter(
            func.lower(DepartmentModel.dept_no).contains(q.lower())
            | func.lower(DepartmentModel.dept_name).contains(q.lower()))


class Employee(ActiveSQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interface = (relay.Node, )

    def get_by_emp_no(query, emp_no):
        return query.filter_by(emp_no=emp_no).first()


class EmployeeConnection(relay.Connection):
    class Meta:
        node = Employee

    total_count = Int()

    def resolve_total_count(root, info):
        return root.length


class EmployeeFilter(FilterSet):
    is_manager = graphene.Boolean()

    class Meta:
        model = EmployeeModel
        fields = {
            'emp_no': ['eq', 'in', 'ilike', 'range'],
            'birth_date': ['eq', 'ilike', 'in', 'range'],
            'first_name': ['eq', 'ilike', 'in'],
            'last_name': ['eq', 'ilike', 'in'],
            'gender': ['eq'],
            'hire_date': ['eq', 'ilike', 'in', 'range'],
        }

    @classmethod
    def is_manager_filter(cls, info, query, value):
        query = query.outerjoin(
            DeptManagerModel,
            EmployeeModel.emp_no == DeptManagerModel.emp_no).distinct()

        if value:
            filter_ = DeptManagerModel.emp_no.isnot(None)
        else:
            filter_ = DeptManagerModel.emp_no.is_(None)

        return query, filter_


class Query(ObjectType):
    node = relay.Node.Field()
    '''Department's queries'''
    departments = List(Department, q=String())

    def resolve_departments(self, info, **args):
        q = args.get("q")
        return Department.filter_by_q(query=Department.query(info), q=q or '')

    department = Field(Department, dept_no=String(required=True))

    def resolve_department(self, info, **args):
        dept_no = args.get("dept_no")
        return Department.get_by_dept_no(query=Department.query(info),
                                         dept_no=dept_no)

    '''Employee's queries'''
    employees = FilterableConnectionField(EmployeeConnection,
                                          filters=EmployeeFilter())

    employee = Field(Employee, emp_no=String(required=True))

    def resolve_employee(self, info, emp_no):
        return Employee.get_by_emp_no(query=Employee.query(info),
                                      emp_no=emp_no)


schema = graphene.Schema(query=Query, types=[Department, Employee])
