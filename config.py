from decouple import config
from os import environ


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = environ.get("KEY")
    BCRYPT_LOG_ROUNDS = 12


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False
