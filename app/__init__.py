import os
from flask import Flask
from app.config import CIConfig, DevelopmentConfig, ProductionConfig, TestingConfig
from app.models import db

CONFIG_MAPPER = {
    'ci': CIConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}


def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV')
    try:
        app.config.from_object(CONFIG_MAPPER[env])
    except KeyError:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    from app.views import api
    app.register_blueprint(api)

    return app
