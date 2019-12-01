import mock
import sys
from app.config import get_aws_rds
from publics import TESTING_DB


@mock.patch.dict(sys.modules, {'secrets': None})
def test_get_aws_rds():
    assert get_aws_rds() == TESTING_DB
