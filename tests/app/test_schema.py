from graphene.test import Client
from app.schema import schema
from app import app

app.app_context().push()
client = Client(schema)


def test_departments(snapshot):
    query = """
        {
          departments {
            deptNo
            deptName
          }
        }
    """
    snapshot.assert_match(client.execute(query))


def test_department(snapshot):
    query = """
        {
          department(deptNo: "d003"){
            deptNo
            deptName
          }
        }
    """
    snapshot.assert_match(client.execute(query))


def test_employees(snapshot):
    query = """
        {
          employees(
            filters: {
              isManager: true
              or: [
                {empNoRange: { begin: "10030", end: "10050" }}
                {lastNameIlike: "a%"}
                {firstNameIlike: "b%"}
                {gender: "F"},
                {birthDateRange: { begin: "1964-02-01", end: "1974-02-01"}}
              ]}
            first: 10
            sort: [LAST_NAME_ASC, FIRST_NAME_ASC]
          ){
            totalCount
            edges{
              node{
                empNo
                birthDate
                firstName
                lastName
                gender
                hireDate
              }
            }
            pageInfo{
              hasPreviousPage,
              hasNextPage,
              startCursor,
              endCursor,
            }
          }
        }
    """

    # Case isManager is True
    snapshot.assert_match(client.execute(query))

    # Case isManager is False
    query_is_manager_is_false = """
        {
          employees(
            filters: {
              isManager: false
            }
          ){
            edges{
              node{
                empNo
              }
            }
          }
        }
    """
    snapshot.assert_match(client.execute(query_is_manager_is_false))


def test_employee(snapshot):
    query = """
        {
          employee(empNo: "10003"){
            empNo
            firstName
            lastName
          }
        }
    """
    snapshot.assert_match(client.execute(query))
