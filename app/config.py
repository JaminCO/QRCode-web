import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI")
    DEBUG=True
    ENV="development"


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")
    ENV="testing"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres", "postgresql")
    ENV="production"


config = {
    "development": DevelopmentConfig,
    "testing": TestConfig,
    "production": ProductionConfig,

    "default": ProductionConfig
}
