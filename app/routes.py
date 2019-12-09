from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Hamlet'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'It is a very rainy day in New York City today.'
        },
        {
            'author': {'username': 'Peter'},
            'body': 'How about the news about the impeachment?!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
