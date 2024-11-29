import unittest
from dashboard.app import app

class TestDashboard(unittest.TestCase):
    def test_app_running(self):
        client = app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
