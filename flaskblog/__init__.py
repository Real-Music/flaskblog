from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # ORM
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '37e88810d98a26cfbef850f976986f74'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #route guard
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_POST'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'fedjioraymondtest@gmail.com'
app.config['MAIL_PASSWORD'] = 'pdjpxad47'
mail = Mail(app)

from flaskblog import route
