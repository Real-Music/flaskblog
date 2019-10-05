from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy  # ORM
from form import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '37e88810d98a26cfbef850f976986f74'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

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


if __name__ == '__main__':
    app.run(debug=True)
