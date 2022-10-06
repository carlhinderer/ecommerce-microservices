import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    pg_user = os.environ["POSTGRES_USER"]
    pg_pw = os.environ["POSTGRES_PASSWORD"]
    pg_host = os.environ["POSTGRES_HOSTNAME"]
    pg_port = os.environ["POSTGRES_PORT"]
    pg_db = os.environ["APPLICATION_DB"]

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{pg_user}:{pg_pw}@{pg_host}:{pg_port}/{pg_db}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    """Production Configuration"""


class DevelopmentConfig(Config):
    """Development Configuration"""


class TestingConfig(Config):
    """Testing Configuration"""
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
