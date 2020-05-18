import unittest
from blog.models import Quotes

class testQuotes(unittest.TestCase):
    def setUp(self):
        self.new_quote = Quotes('morimga','Coding can be fun',"http://github.com/owinlawrence")

    def test_instance_variables(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))