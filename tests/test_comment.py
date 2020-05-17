import unittest
from app.models import Blog,Comment
from app import db
from datetime import datetime

class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blog(id=40, title='New Blog', content='This is the content', category ='Travel', posted=datetime.now())
        self.new_comment = Comment(name='Test Comment', comment='This is my Test comment',blog=new_blog)

    def tearDown(self):
        db.session.delete(self.new_blog)
        db.session.commit()
        db.session.delete(self.new_comment)
        db.session.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.name,'Test Comment')
        self.assertEquals(self.new_comment.comment,'This is my Test comment')
        self.assertEquals(self.new_comment.blog, new_blog)
