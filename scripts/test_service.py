import requests
from requests.auth import HTTPBasicAuth
import unittest

class TestIntegration(unittest.TestCase):

    def test_health_endpoint(self):
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

    def test_user_registration(self):
        user_data = {
            "username": "testuser",
            "password": "password123",
            "email": "testuser@example.com"
        }

        response = requests.post('http://localhost:8080/users/register', json=user_data)
        print("Register User Response:", response.status_code, response.content)
        self.assertEqual(response.status_code, 201)  # Expecting HTTP 201 Created

    def test_user_login(self):
        login_data = {
            "username": "testuser",
            "password": "password123"
        }

        response = requests.post('http://localhost:8080/users/login', json=login_data)
        print("Login User Response:", response.status_code, response.content)
        self.assertEqual(response.status_code, 200)  # Expecting HTTP 200 OK

if __name__ == '__main__':
    unittest.main()
