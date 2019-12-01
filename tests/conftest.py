import pytest

from app import create_app
from db.populate_mocks import populate_mocks


@pytest.fixture
def client():
    app = create_app()

    from app.models import db
    with app.app_context():
        populate_mocks(db)

    with app.test_client() as client:
        yield client
