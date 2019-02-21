import unittest
from app.models import review

class TestReview(unittest.TestCase):
    """
    A class I will use to test the reviews
    """

    def setUp(self):
        """
        This will create a new review before each test
        """
        self.new_review = Review(title = "")

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Review.query.delete()

    def test_is_instance(self):
        """
        This will test whether the review created is an instance of the review class
        """
        self.assertTrue(isinstance(self.new_review, Review))

    def test_init(self):
        """
        Checks whether the new_review test is instantiated correctly
        """
        self.assertTrue(self.new_review.title == "")

    def test_save_review(self):
        """
        This will test whether the review is added to the db
        """
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all()) > 0)
    
   