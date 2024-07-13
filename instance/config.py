""" contains links to database connections, ie.,mysql
    mail client, ie.gmail, yahoo,
    also hold the secret key used wit form validations
"""

import os

class Config:
    SECRET_KEY = '89cf297f4b4634754cd052c1'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://MUSTAFA:5m9l<18>_X!@localhost/gamer'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://MUSTAFA:5m9l<18>_X!@localhost/gamer'
    

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://MUSTAFA:5m9l<18>_X!@localhost/gamer'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://MUSTAFA:5m9l<18>_X!@localhost/gamer'
    

config = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'production': ProductionConfig,
'default': DevelopmentConfig
}