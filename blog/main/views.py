from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from blog.models import Role, Blog, Comment, Subscriber, User
from .forms import UpdateProfile, CommentForm, BlogForm, SubscribeForm
from flask_login import login_required, current_user
from wtforms import Form
from blog import db
from blog.requests import get_Quotes


@main.route("/")
@main.route("/home")
def home():
    quotes=get_Quotes()
    print(quotes)
    sports = Blog.get_blogs('Sports-Blog')
    travel = Blog.get_blogs('Travel-Blog')
    fitness = Blog.get_blogs('Fitness-Blog')
    fashion = Blog.get_blogs('Fashion-Blog')
    food = Blog.get_blogs('Food-Blog')
    politics = Blog.get_blogs('Political-Blog')

    return render_template('home.html', sports = sports, travel = travel, fitness = fitness, fashion = fashion, food = food, quotes = quotes)
@main.route('/user/<username>')
def profile(username):
    user = User
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

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
    return render_template('profile/profile.html', title='Account',
                            form=form)

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

    flash('Your blog has been deleted')
    return redirect(url_for('main.home'))
    
    return render_template('blogs.html', id=id, blog = blog)

@main.route('/blog/comment/delete/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_comment(id): 
    comment = Comment.query.filter_by(id=id).first()
    blog_id = comment.blog
    Comment.delete_comment(id)

    flash('Comment has been deleted')
    return redirect(url_for('main.blog',id=blog_id))

@main.route('/blogs/sports')
def sports():
    blogs = Blog.get_blogs('Sports-Blog')

    return render_template('sports.html',blogs = blogs)

@main.route('/blogs/travel')
def travel():
    blogs = Blog.get_blogs('Travel-Blog')

    return render_template('travel.html',blogs = blogs)


@main.route('/blogs/fitness')
def fitness():
    blogs = Blog.get_blogs('Fitness-Blog')

    return render_template('fitness.html',blogs = blogs)

@main.route('/blogs/fashion')
def fashion():
    blogs = Blog.get_blogs('Fashion-Blog')

    return render_template('fashion.html',blogs = blogs)

@main.route('/blogs/food')
def food():
    blogs = Blog.get_blogs('Food-Blog')

    return render_template('food.html',blogs = blogs)

@main.route('/blogs/politics')
def politics():
    blogs = Blog.get_blogs('Political-Blog')

    return render_template('politics.html',blogs = blogs)

@main.route('/blogs/latest', methods = ['GET','POST'])
def latest_blogs():
    blogs = Blog.query.order_by(Blog.posted.desc()).all()

    return render_template('latest_blog.html',blogs = blogs)

@main.route('/subscription',methods=['GET','POST'])
def subscription():
    subscription_form = SubscribeForm()

    if subscription_form.validate_on_submit():
        new_subscriber = Subscriber(subscriber_name=subscription_form.subscriber_name.data,subscriber_email=subscription_form.subscriber_email.data)

        db.session.add(new_subscriber)
        db.session.commit()

        return redirect(url_for('main.home'))    

    return render_template('subscription.html',subscription_form = subscription_form)