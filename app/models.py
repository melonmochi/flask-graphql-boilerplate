from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String

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
            'id': self.dept_no,
            'name': self.dept_name,
        }

    def __repr__(self):
        return '<Departments %r>' % self.dept_name
