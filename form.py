from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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
    submit = SubmitField('Log up')
