import os
from dotenv import load_dotenv

dotenv_file_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add other configuration options here


class DevelopmentConfig(Config):
    ENV = "development  "
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:mysql68646724@localhost:3306/facturas"
    )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")
    # Add other testing-specific configuration options here


class ProductionConfig(Config):
    # Add production-specific configuration options here
    pass
