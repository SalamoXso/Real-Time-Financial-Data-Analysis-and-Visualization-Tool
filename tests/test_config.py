import pytest
import unittest
from config import config

class TestConfig(unittest.TestCase):
    def test_config_loading(self):
        self.assertEqual(config.get('DEBUG'), True)  # Adjust based on your dev_config.yaml

if __name__ == '__main__':
    unittest.main()
