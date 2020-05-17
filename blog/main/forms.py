from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, Email, DataRequired, Length
from flask_wtf.file import FileAllowed, FileField
from flask_login import current_user

class UpdateProfile(FlaskForm):
    username = StringField('Username')
    email = StringField('Email', Email)
    bio = TextAreaField('Tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Blog Title',validators=[Required()])
    blog_body = TextAreaField('Write Blog Content',validators=[Required()])
    blog_category = SelectField('Blog Category',choices=[('Sports-Blog','Sports'),('Travel-Blog','Travel'),('Fitness-Blog','Fitness'),('Fashion-Blog','Fashion'),('Food-Blog','Food'),('Political-Blog','Politics')],validators=[Required()])
    submit = SubmitField('Submit Blog')

class CommentForm(FlaskForm):
    name = StringField('Enter Your Name',validators=[Required()])
    comment = TextAreaField('Comments', validators=[Required()])
    submit = SubmitField('Submit Comment')

class SubscribeForm(FlaskForm):
    subscriber_name = StringField('Enter your Full Name',validators=[Required()])
    subscriber_email = StringField('Enter your Email',validators=[Required(),Email()])
    submit = SubmitField('Subscribe')
