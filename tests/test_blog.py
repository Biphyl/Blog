import unittest
from blog.models import Blog
from blog import db
from datetime import datetime

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blog(id=40, title='New Blog', content='This is the content', category ='Travel', posted=datetime.now())

    def tearDown(self):
        db.session.add(self.new_blog)
        db.session.commit()
        db.session.delete(self.new_blog)
        db.session.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title,'New Blog')
        self.assertEquals(self.new_blog.content,'This is the content')
        self.assertEquals(self.new_blog.category,'Travel')
        self.assertEquals(self.new_blog.posted,datetime.now(2020, 5, 12, 3, 18, 5, 590964))


    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        blog = Blog.get_blog(40)
        self.assertTrue(blog is not None)
