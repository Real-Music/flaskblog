from flask import Flask, render_template, url_for

app = Flask(__name__)

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


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
