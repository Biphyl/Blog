from flask import Flask, Blueprint


main = Blueprint('main',__name__)


from blog.main import views