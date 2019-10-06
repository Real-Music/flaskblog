from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '12345678':
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', tiltle='Login', form=form)
