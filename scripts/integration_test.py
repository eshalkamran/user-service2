import requests
import unittest

class TestIntegration(unittest.TestCase):

    def test_user_service(self):
        response = requests.get(
            'http://localhost:8080/health',
            auth=('admin', 'secret')  # Replace with actual username and password
        )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
