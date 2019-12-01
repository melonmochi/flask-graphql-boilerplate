from publics import CI_DB, TESTING_DB


def get_aws_rds():
    try:
        from secrets import AWS_RDS_DB
    except ImportError:
        AWS_RDS_DB = None
    return AWS_RDS_DB


def db_url(connect_args):
    user, pw, host, port, db = connect_args['user'], connect_args[
        'pw'], connect_args['host'], connect_args['port'], connect_args['db']
    return f'postgresql://{user}:{pw}@{host}:{port}/{db}'


# DB URLS for each Environment
class Config(object):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class CIConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = db_url(CI_DB)


class DevelopmentConfig(Config):
    DB = get_aws_rds()

    if DB is None:
        DB = TESTING_DB

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = db_url(DB)


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = db_url(TESTING_DB)
