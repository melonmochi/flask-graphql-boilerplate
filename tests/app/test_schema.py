from graphene.test import Client
from app.schema import schema


def test_department(snapshot):
    client = Client(schema)
    query = """
        {
          departments {
            totalCount
            edges {
              node {
                deptNo
              }
            }
          }
        }
    """
    snapshot.assert_match(client.execute(query))
