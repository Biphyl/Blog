import os

class Config:

    SECRET_KEY = 'Lovine'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2:/biron:Biron4745@localhost/blogs'
    QUOTES_API = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')





class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/blogs'
    DEBUG = True



class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/blogs'
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/blogs'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}