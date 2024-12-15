from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {"username":"Eber"}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in portlan!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Hi post from susan'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)