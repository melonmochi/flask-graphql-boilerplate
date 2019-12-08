from publics import CI_DB, TESTING_DB


def get_db():
    ''' Try to get user's own database'''
    try:
        from secrets import DB
    except ImportError:
        DB = TESTING_DB
    return DB


def db_url(connect_args):
    user, pw, host, port, db = connect_args['user'], connect_args[
        'pw'], connect_args['host'], connect_args['port'], connect_args['db']
    return f'postgresql://{user}:{pw}@{host}:{port}/{db}'


# DB URLS for each Environment
class Config(object):
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class CIConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = db_url(CI_DB)


class DevelopmentConfig(Config):
    DB = get_db()
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = db_url(DB)


class ProductionConfig(Config):
    DB = get_db()
    SQLALCHEMY_DATABASE_URI = db_url(DB)


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = db_url(TESTING_DB)
