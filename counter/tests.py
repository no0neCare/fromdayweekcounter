from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.


class TestCalls(TestCase):
    def test_call_view_correct_date(self):
        data = {'date': '30.01.2021'}
        response = self.client.post('/counter/counter/', data)
        self.assertEqual(response.status_code, 200)

    def test_call_view_wrong_date(self):
        data = {'date': '32.01.2021'}
        response = self.client.post('/counter/counter/', data)
        self.assertEqual(response.status_code, 400)
