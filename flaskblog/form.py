from flaskblog.models import User, Post
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


# Sigu Up Form
class RegistrationForm(FlaskForm):
    # username Validation
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])

    # Email Validation
    email = StringField('Email', validators=[DataRequired(), Email()])

    # Password Validation
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8, max=32)])
    # Confrim Password
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])

    # Submit Button
    submit = SubmitField('Sign up')

    # Check if username already exist
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'Username already exist. Choose another name.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exist.')


# Login Form
class LoginForm(FlaskForm):
    # Email Validation
    email = StringField('Email', validators=[DataRequired(), Email()])

    # Password Validation
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8, max=32)])
    # Token
    remember = BooleanField('Remember Me')

    # Submit Button
    submit = SubmitField('Log in')


class UpdateAccountForm(FlaskForm):
    # username Validation
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    # Email Validation
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    # Submit Button
    submit = SubmitField('Update')

    # Check if username already exist
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'Username already exist. Choose another name.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email already exist.')

# New Post
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')