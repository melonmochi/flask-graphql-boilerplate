from pathlib import Path

folder_path = Path(__file__).parent


def excute_sql(db, script_file):
    script_path = folder_path / script_file
    with script_path.open() as script:
        script_sql = script.read()
        db.session.execute(script_sql)


def populate_mocks(db):
    '''CREATE schemas'''
    excute_sql(db, "schemas.sql")
    '''TABLE employees'''
    excute_sql(db, "employees.sql")
    '''TABLE departments'''
    excute_sql(db, "departments.sql")
    '''TABLE dept_emp'''
    excute_sql(db, "dept_emp.sql")
    '''TABLE dept_manager'''
    excute_sql(db, "dept_manager.sql")
    '''TABLE titles'''
    excute_sql(db, "titles.sql")
    '''TABLE salaries'''
    excute_sql(db, "salaries.sql")

    db.session.commit()
