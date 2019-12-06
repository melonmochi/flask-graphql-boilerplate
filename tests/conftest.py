import pytest

from app import app
from db.populate_mocks import populate_mocks


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            from app.models import db
            populate_mocks(db)
        yield client
