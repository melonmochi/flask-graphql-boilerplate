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
    print('os env is', env)
    try:
        app.config.from_object(CONFIG_MAPPER[env])
    except KeyError:
        app.config.from_object(DevelopmentConfig)

    print('app.config.db is', app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)

    from app.views import api
    app.register_blueprint(api)

    return app
