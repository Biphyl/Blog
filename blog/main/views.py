from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from blog.models import Post, Blog, Comment, Subscriber
from .forms import UpdateProfile, CommentForm, BlogForm, SubscribeForm
from flask_login import  login_required, current_user
import json



@main.route("/")
@main.route("/home")
def home():

    random = request.get('http://quotes.stormconsultancy.co.uk/random.json').json

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/account", methods=['GET', 'POST'])
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
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='photos/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)