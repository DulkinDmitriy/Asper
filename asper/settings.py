import os


class Config:
    """Base configuration."""

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class ProductionConfig(Config):
    """Production configuration."""

    ENV = 'production'
    DEBUG = False


class DevelopmentConfig(Config):
    """Development configuration."""

    ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration."""

    ENV = 'test'
    TESTING = True
    DEBUG = True
