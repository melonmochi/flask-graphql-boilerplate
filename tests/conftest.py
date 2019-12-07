import pytest

from app import app as flask_app
from db.populate_mocks import populate_mocks


@pytest.fixture
def app():
    app = flask_app
    with app.app_context():
        from app.models import db
        populate_mocks(db)
    return app
