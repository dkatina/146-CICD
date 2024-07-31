import unittest
from faker import Faker
from app import app


class TestAPI(unittest.TestCase): #inheriting testcase functionality from unittest

    def setUp(self):
        self.app = app.test_client() #initializing test app as a test client

    #tests go below

    def test_sum(self):
        payload = {'num1': 2, 'num2': 3}
        response = self.app.post('/sum', json=payload) #Sending a mock post request to our app's testing client's /sum route with a payload
        data = response.get_json()
        self.assertEqual(data['result'], 5)

    def test_random_sum(self):
        fake = Faker()
        num1 = fake.random_number(digits=3) #Creating mock (random) data for num1 
        num2 = fake.random_number(digits=3)
        payload = {'num1': num1, 'num2': num2}
        response = self.app.post('/sum', json=payload) #Sending a mock post request to our app's testing client's /sum route with a payload
        data = response.get_json()
        self.assertEqual(data['result'], num1+num2)
       

if __name__ == '__main__':
    unittest.main()