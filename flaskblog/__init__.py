from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # ORM

app = Flask(__name__)
app.config['SECRET_KEY'] = '37e88810d98a26cfbef850f976986f74'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import route