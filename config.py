import os


# Default config.
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "be kind"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
