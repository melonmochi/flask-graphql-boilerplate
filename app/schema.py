from graphene import Boolean, Int, Field, List, ObjectType, relay, Schema, String
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from sqlalchemy.sql.expression import func
from app.models import DepartmentModel, DeptEmpModel, DeptManagerModel, EmployeeModel


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

    def get_by_dept_no(info, dept_no):
        return Department.query(info).filter_by(dept_no=dept_no).first()

    def filter_by_q(info, q):
        return Department.query(info).filter(
            func.lower(DepartmentModel.dept_no).contains(q.lower())
            | func.lower(DepartmentModel.dept_name).contains(q.lower()))


class Employee(ActiveSQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interface = (relay.Node, )

    department = Field(Department)
    is_manager = Boolean()

    def resolve_department(self, info):
        dept_no = DeptEmp.query(info).filter(
            DeptEmpModel.emp_no == self.emp_no).first().dept_no
        return Department.get_by_dept_no(info=info, dept_no=dept_no)

    def resolve_is_manager(self, info):
        return DeptManager.query(info).filter_by(
            emp_no=self.emp_no).first() is not None

    def get_by_emp_no(info, emp_no):
        return Employee.query(info).filter_by(emp_no=emp_no).first()


class EmployeeConnection(relay.Connection):
    class Meta:
        node = Employee

    total_count = Int()

    def resolve_total_count(root, info):
        return root.length


class EmployeeFilter(FilterSet):
    is_manager = Boolean()

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


class DeptEmp(ActiveSQLAlchemyObjectType):
    class Meta:
        model = DeptEmpModel
        interface = (relay.Node, )


class DeptManager(ActiveSQLAlchemyObjectType):
    class Meta:
        model = DeptManagerModel
        interface = (relay.Node, )


class Query(ObjectType):
    node = relay.Node.Field()
    '''Department's queries'''
    departments = List(Department, q=String())
    department = Field(Department, dept_no=String(required=True))

    def resolve_departments(self, info, **args):
        q = args.get("q")
        return Department.filter_by_q(info=info, q=q or '')

    def resolve_department(self, info, **args):
        dept_no = args.get("dept_no")
        return Department.get_by_dept_no(info=info, dept_no=dept_no)

    '''Employee's queries'''
    employees = FilterableConnectionField(EmployeeConnection,
                                          filters=EmployeeFilter())
    employee = Field(Employee, emp_no=String(required=True))

    def resolve_employee(self, info, **args):
        emp_no = args.get("emp_no")
        return Employee.get_by_emp_no(info=info, emp_no=emp_no)


schema = Schema(query=Query, types=[Department, Employee])
