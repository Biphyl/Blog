from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, Email, DataRequired, Length
from flask_wtf.file import FileAllowed, FileField

class UpdateProfile(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

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
