import mock
import os
from app.utils import config_app
from app import app


@mock.patch.dict(os.environ, {'FLASK_ENV': 'NOT_DEFINED_ENV'})
def test_env_is_not_defined():
    config_app(app)
