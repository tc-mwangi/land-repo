import unittest
from app.models import User
from app import db


class TestUSer(unittest.TestCase):
    """
    A class for testing the user
    """
    def setUp(self):
        """
        creates a new user before  a test
        """
        self.new_user = User(username = "user",bio = "newUser",password ="1234")

    def tearDown(self):
        """
        This will clear the db after each test
        """
        User.query.delete()
        
    def test_is_instance(self):
        """
        Tests whether the user created is an instance of the User class
        """
        self.assertTrue(isinstance(self.new_user, User))

    def test_init(self):
        """
        Tests whether the user is instantiated correctly
        """
        self.assertTrue(self.new_user.username == "user")
        self.assertTrue(self.new_user.bio == "newUser")

    def test_pass_generate(self):
        """
         Tests whether a new password is generated for the user
        """
        self.assertTrue(self.new_user.user_pass is not None)
    
    def test_hash_generate(self):
        """
        Tests whether the password generated is not equal to the original password
        """
        self.assertTrue(self.new_user.user_pass is not "1234")
    
    def test_save_user(self):
        """
        Tests whether the user is saved to the db
        """
        self.new_user.save_user()
        self.assertTrue(len(User.query.all()) == 1)
