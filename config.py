import os


# Default config.
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "\x8b9\xbfCK`\xa1^\xe7y\xfc\xc2\x7f\xa1\xd8R\xf3I\xd3\xddR\xcb&8#"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
