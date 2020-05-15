import os

class Config:

    SECRET_KEY = 'Lovine'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/blogs'






class DevConfig(Config):

    DEBUG = True



class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = 


config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}