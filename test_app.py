import unittest
from app import greet, add

class TestApp(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
