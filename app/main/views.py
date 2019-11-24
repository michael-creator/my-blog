from flask import Flask, render_template, url_for
from . import main 



posts = [
    {
        'author': 'mikel karije',
        'title': 'funny blog',
        'content': '1blog  content',
        'date_posted': 'april 22, 2019'
    },
     {
        'author': 'mikel karije',
        'title': 'social blog',
        'content': '2blog  content',
        'date_posted': 'april 22, 2019'
    },
      {
        'author': 'john dumelo',
        'title': 'business blog',
        'content': '3blog  content',
        'date_posted': 'april 22, 2019'
    }
]

@main.route('/')
def index():
    return render_template('index.html', posts=posts)

@main.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@main.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Rgister', form=form)