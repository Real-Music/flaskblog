from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # ORM
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '37e88810d98a26cfbef850f976986f74'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #route guard
login_manager.login_message_category = 'info'

from flaskblog import route