import mock
import os
from app import create_app


@mock.patch.dict(os.environ, {'FLASK_ENV': 'NOT_DEFINED_ENV'})
def test_env_is_not_defined():
    create_app()
