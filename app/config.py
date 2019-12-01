# DB URLS for each Environment
class Config(object):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class CIConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class DevelopmentConfig(Config):
    from secrets import AWS_RDS_DB
    aws_rds_user, aws_rds_pw, aws_rds_host, aws_rds_port, aws_rds_db = AWS_RDS_DB[
        'user'], AWS_RDS_DB['pw'], AWS_RDS_DB['host'], AWS_RDS_DB[
            'port'], AWS_RDS_DB['db']
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'postgresql://\
      {aws_rds_user}:{aws_rds_pw}@{aws_rds_host}:{aws_rds_port}/{aws_rds_db}'


class TestingConfig(Config):
    from publics import TESTING_DB
    user, pw, host, port, db = TESTING_DB['user'], TESTING_DB[
        'pw'], TESTING_DB['host'], TESTING_DB['port'], TESTING_DB['db']
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{pw}@{host}:{port}/{db}'
