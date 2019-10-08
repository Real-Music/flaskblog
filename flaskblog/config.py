import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '37e88810d98a26cfbef850f976986f74'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_POST = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'fedjioraymondtest@gmail.com'
    MAIL_PASSWORD = 'pdjpxad47'