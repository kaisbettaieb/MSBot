class ProductionConfig():
    ENV = 'production'
    DEBUG = False
    SECRET_KEY = 'bnsdquf5fdhptrzmv5dfslkf9ez9erzpld'

class DevelopmentConfig():
    ENV = 'development'
    DEBUG = True

class TestingConfig():
    TESTING = True
    DEBUG = True
    ENV = 'testing'