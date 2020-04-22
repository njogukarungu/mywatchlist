import unittest
from app.models import Review
class ReviewTest(unittest.TestCase):
    def setUp(self):
        self.newReview = Review(1234, 'Python Thriller', '/373t338', "an awesome one")
    def test_instance(self):
        self.assertTrue(isinstance(self.newReview, Review))
