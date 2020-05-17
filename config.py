import os

class Config:

    SECRET_KEY = 'Lovine'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False





class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/blogs'
    DEBUG = True



class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/blogs'


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}