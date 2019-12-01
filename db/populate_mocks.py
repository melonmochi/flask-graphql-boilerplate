from pathlib import Path

db_path = Path(__file__).parent


def populate_mocks(db):
    '''CREATE schemas'''
    schemas_path = db_path / "schemas.sql"
    with schemas_path.open() as schemas:
        schemas_sql_scripts = schemas.read()
        db.session.execute(schemas_sql_scripts)
    '''TABLE employees'''
    employees_path = db_path / "employees.sql"
    with employees_path.open() as emp:
        emp_sql_scripts = emp.read()
        db.session.execute(emp_sql_scripts)
    '''TABLE departments'''
    departments_path = db_path / "departments.sql"
    with departments_path.open() as dep:
        dep_sql_scripts = dep.read()
        db.session.execute(dep_sql_scripts)

    db.session.commit()
