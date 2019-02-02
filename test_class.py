import unittest

from flask import jsonify, json
from handler import app



class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_hello_world(self):
        resp = self.app.get('/')
        data = json.loads(resp.get_data(as_text=True))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['message'], 'Hello, world')

    def test_get_status(self):
        resp = self.app.get('/status')
        data = json.loads(resp.get_data(as_text=True))
        self.assertEqual(resp.status_code, 200)
        self.assertRegex(data['status'], "^[a-zA-Z ]*$") # check for text with spaces

        

