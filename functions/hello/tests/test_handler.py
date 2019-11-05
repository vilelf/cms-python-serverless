import json
import unittest
from functions.hello.main import hello


class HelloHandlerTest(unittest.TestCase):
    def test_hello(self):
        expected = '{"message": "Hello world, serverless!!"}'
        actual = hello({}, {})['body']
        self.assertEqual(actual, expected)
