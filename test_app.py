import unittest
import json
from app import app
from users import User
from products import Product

class FlaskApiTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    # # Helper function to get authentication token for a user
    # def get_token(self, username, password):
    #     response = self.app.post('/login', data=json.dumps({'username': username, 'password': password}),
    #                              content_type='application/json')
    #     data = json.loads(response.get_data(as_text=True))
    #     return data.get('token')

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user_not_found(self):
        response = self.app.get('/users/nonexistentuser')
        self.assertEqual(response.status_code, 404)

    # def test_create_user(self):
    #     response = self.app.post('/users', data=json.dumps({'username': 'newuser', 'password': 'password', 'deposit': 0, 'role': 'buyer'}),
    #                              content_type='application/json')
    #     self.assertEqual(response.status_code, 201)

    
    def test_update_user_unauthorized(self):
        response = self.app.put('/users', data=json.dumps({'deposit': 100}), content_type='application/json')
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()
