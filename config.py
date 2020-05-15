import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/blogs'





class DevConfig(Config):





class ProdConfig(Config):

