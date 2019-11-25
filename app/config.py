from secrets import POSTGRES

user, pw, host, port, db = POSTGRES['user'], POSTGRES['pw'], POSTGRES[
    'host'], POSTGRES['port'], POSTGRES['db']


class Config(object):
    DEVELOPMENT = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{pw}@{host}:{port}/{db}'
