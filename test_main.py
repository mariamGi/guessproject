import unittest
from main import add_number


class TestMain(unittest.TestCase):
    def test_adding(self):
        self.assertEqual(6, add_number(5, 1))
