from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Date, Integer, String

db = SQLAlchemy()


#  Departments Model
class Departments(db.Model):
    __tablename__ = 'departments'

    dept_no = Column(String(4), primary_key=True)
    dept_name = Column(String(40), unique=True, nullable=False)

    def __init__(self, dept_no, dept_name):
        self.dept_no = dept_no
        self.dept_name = dept_name

    @property
    def serializable(self):
        return {
            'dept_no': self.dept_no,
            'name': self.dept_name,
        }

    def __repr__(self):
        return '<Departments %r>' % self.dept_name


#  Employees Model
class Employees(db.Model):
    __tablename__ = 'employees'

    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(String(1))
    hire_date = Column(Date, nullable=False)

    def __init__(self, emp_no, birth_date, first_name, last_name, gender,
                 hire_date):
        self.emp_no = emp_no
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.hire_date = hire_date

    @property
    def serializable(self):
        return {
            'emp_no': self.emp_no,
            'birth_date': self.birth_date,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'hire_date': self.hire_date,
        }

    def __repr__(self):
        return '<Employees %r>' % self.first_name
