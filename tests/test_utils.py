
import pytest
import unittest
from utils.api_helpers import make_request

class TestUtils(unittest.TestCase):
    def test_api_helper(self):
        response = make_request('https://jsonplaceholder.typicode.com/todos/1')
        self.assertIsNotNone(response)
        self.assertIn('userId', response)
        self.assertEqual(response.get('userId'), 1)

if __name__ == '__main__':
    unittest.main()
