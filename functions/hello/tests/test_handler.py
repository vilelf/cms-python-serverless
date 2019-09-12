import unittest
from functions.hello import hello


class TestHelloHandler(unittest.TestCase):
    def test_hello(self):
        expected = 'Hello world, serverless!!'
        actual = hello({}, {})
        self.assertEqual(actual, expected)
