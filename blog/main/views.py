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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

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

@main.route('/new-blog', methods = ['GET','POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog = blog_form.blog_body.data
        category = blog_form.blog_category.data

        new_blog = Blog(title = title, content = blog, category = category,user = current_user)
        new_blog.save_blog()

        return redirect(url_for('main.home'))

    title = 'New Blog'
    return render_template('new_blog.html', title = title, blog_form = blog_form)

@main.route('/blog/<int:id>', methods = ["GET","POST"])
def blog(id):
    blog = Blog.get_blog(id)
    posted_date = blog.posted.strftime('%b %d, %Y')

    comment_form = CommentForm()
    if comment_form.validate_on_submit():

        name = comment_form.name.data
        comment = comment_form.comment.data

        new_comment = Comment(name = name, comment = comment, blogit = blog)
        new_comment.save_comment()

        return redirect(url_for('main.blog',id=id))
    
    comments = Comment.get_comments(blog)
    return render_template('blogs.html', blog = blog, comment_form = comment_form, comments = comments, date = posted_date)

@main.route('/blog/<int:id>/update', methods = ['GET','POST'])
@login_required
def update_blog(id):
    blog = Blog.get_blog(id)
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.blog_body.data
        blog.category = form.blog_category.data
        db.session.commit()
        return redirect(url_for('main.blog', id = id))
    elif request.method == 'GET':
        form.title.data = blog.title
        form.blog_body.data = blog.content
        form.blog_category.data = blog.category
    return render_template('new_blog.html', blog_form = form, id=id)

@main.route('/blog/delete/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_blog(id):
    blog = Blog.get_blog(id)
    db.session.delete(blog)
    db.session.commit()

    flash('Blog has been deleted')
    return redirect(url_for('main.home'))
    
    return render_template('blogs.html', id=id, blog = blog)