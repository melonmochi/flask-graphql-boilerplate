from app.models import Department, Employee


def test_department():
    department = Department('d001', 'Marketing')
    assert department.dept_no == 'd001'
    assert department.dept_name == 'Marketing'
    assert department.__repr__() == "<Department 'Marketing'>"


def test_employee():
    department = Employee(10001, 'Wed, 02 Sep 1953 00:00:00 GMT', 'Georgi',
                          'Simmel', 'M', 'Thu, 26 Jun 1986 00:00:00 GMT')
    assert department.emp_no == 10001
    assert department.birth_date == 'Wed, 02 Sep 1953 00:00:00 GMT'
    assert department.first_name == 'Georgi'
    assert department.last_name == 'Simmel'
    assert department.gender == 'M'
    assert department.hire_date == 'Thu, 26 Jun 1986 00:00:00 GMT'
    assert department.__repr__() == "<Employee 'Georgi'>"
