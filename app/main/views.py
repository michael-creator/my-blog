from flask import Flask, render_template, url_for, flash, redirect, abort,request
from . import main
from .forms import RegistrationForm, LoginForm,UpdateProfile ,PostForm
from flask_login import login_required
from ..models import User
from .. import db,photos

posts = [
    {
        'author': 'dancan dante',
        'title': 'funny blog',
        'content': 'In France, a chemist named Pilatre de Rozier tested the flammability of hydrogen by gulping a mouthful and blowing across an open flame, proving at a stroke that hydrogen is indeed explosively combustible and that eyebrows are not necessarily a permanent feature of one’s face.',
        'date_posted': 'april 22, 2019'
    },
     {
        
        'author': 'mikel karije',
        'title': 'Business blog',
        'content': ' Woody Allen calls the planning portion of writing the “pace the floor” part. If you are an analytical thinker, which many business writers are, this is natural for you, but accept that sometimes it makes your brain hurt as your mind has to figure out all the interconnections. ',
        'date_posted': 'april 22, 2019'
    },
      {
        'author': 'john dumelo',
        'title': 'Health blog',
        'content': 'You can focus your blog on healthy recipes, diets, morning routines, at-home workouts, gym workouts, healthcare tips, and advice – you name it. Lots of opportunities for massive traffic and income here.',
        'date_posted': 'april 22, 2019'
    },
         {
        'author': 'PRofessor',
        'title': 'Inspirational blog',
        'content': 'spreading happiness, simplicity, and clarity in everyone’s lives. Inspirational quotes and articles provided by guest authors and editors enlighten people that are interested in topics related to inner clarity and self-growth.',
        'date_posted': 'april 22, 2019'
    }
]

@main.route('/')
@login_required
def index():
    return render_template('index.html', posts=posts)

@main.route('/login', methods=['GET','_POST_'])
def login():
    form = LoginForm()
    return render_template('login.html', title='LOGIN',form=form)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/post/new',methods = ['GET','POST'])
@login_required
def new_post():
    
    form = PostForm()
    if form.validate_on_submit():
        flash('The Post Has been Updated', 'successful')
        return redirect(url_for('home'))
    return render_template('new_post.html', title='New Post', form=form)