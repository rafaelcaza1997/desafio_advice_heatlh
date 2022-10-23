import os

WORKSPACE = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRETKEY')

    if os.getenv('SQLALCHEMY_DATABASE_URI'):
        SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(WORKSPACE, 'instance', 'app.db')}"
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Prod(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    
class Dev(Config):
    DEBUG = True

class Test(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(WORKSPACE, 'instance', 'test.db')}"
    WTF_CSRF_ENABLED = False
