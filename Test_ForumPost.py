# Author: Leon Xu
# COMP0035: SYSTEMS ENGINEERING
# This is a unit test for the class 'ForumPost'

from unittest import TestCase
import unittest
from Class_ForumPost import ForumPost

class TestForumPost(unittest.TestCase):

    def setup(self):
        self.test_post = ForumPost
        self.test_post.set_name = 'name'


    def test_EditName(self):
        post_name = 'name'
        self.test_post.edit_name(post_name)
        self.assertEqual(post_name, self.test_post.post_name)


if __name__ == '__main__':
    unittest.main()
