import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure session to use filesystem
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'


    #mail configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'service.pimankova@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'drucherato')
    CS50_MAIL_SUBJECT_PREFIX = '[CS50_P1]'
    CS50_MAIL_SENDER = 'CS50 P1 Admin <tomas.flask@gmail.com>'

    FLASKY_ADMIN = os.environ.get('CS50_P1_ADMIN', 'CS50_P1_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite3')
    print(SQLALCHEMY_DATABASE_URI)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite3')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}