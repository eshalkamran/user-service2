import requests
from requests.auth import HTTPBasicAuth
import unittest

class TestIntegration(unittest.TestCase):

    def test_user_service(self):
        print("Sending GET request to /health endpoint with credentials...")

        # Add authentication
        response = requests.get(
            'http://localhost:8080/health',
            auth=HTTPBasicAuth('admin', 'secret')
        )

        print("Received response:")
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")

        self.assertEqual(response.status_code, 200)
        print("Assertion passed: Status code is 200")

if __name__ == '__main__':
    unittest.main()
