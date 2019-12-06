import os
from app.config import CIConfig, DevelopmentConfig, ProductionConfig, TestingConfig

CONFIG_MAPPER = {
    'ci': CIConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}


def config_app(app):
    env = os.getenv('FLASK_ENV')
    try:
        app.config.from_object(CONFIG_MAPPER[env])
    except KeyError:
        app.config.from_object(DevelopmentConfig)
