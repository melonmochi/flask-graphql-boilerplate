import mock
import sys
from app.config import get_db
from publics import TESTING_DB


@mock.patch.dict(sys.modules, {'secrets': None})
def test_get_db():
    assert get_db() == TESTING_DB
