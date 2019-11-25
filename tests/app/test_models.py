from app.models import Departments


def test_departments():
    department = Departments('d001', 'Marketing')
    assert department.dept_no == 'd001'
    assert department.dept_name == 'Marketing'
    assert department.__repr__() == "<Departments 'Marketing'>"
