import os
import datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.form import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Fedjio Raymond',
        'title': 'Blog',
        'content': 'First post blog',
        'post_date': 'July 27, 1996'
    },
    {
        'author': 'Nema Dede',
        'title': 'Blog 2',
        'content': 'Second post blog',
        'post_date': 'January 27, 2019'
    }
]

# Home
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

# About
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        # hash user password
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        # new instance of user
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created. You can now login!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # checking query
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', tiltle='Login', form=form)

# Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    current_date = datetime.datetime.now()
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fin = f_name + current_date.strftime('%d-%m-%Y-%I:%M:%S:%f') + f_ext
    picture_path = os.path.join(app.root_path, 'static/img/profile', picture_fin)
    
    # Resize Image
    img_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(img_size)

    i.save(picture_path)

    return picture_fin

# Account
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename=f'img/profile/{current_user.image_file}' )
    return render_template('account.html', title='Account',image_file=image_file, form = form)

