from django.test import TestCase
from django.urls import resolve,reverse
from hello_app.views import *

# Create your tests here.
# class TestURL(TestCase):
#     def test_signup(self):
#         result=self.client.get('/')
#         print(result)
#         self.assertEqual(result.status_code, 200)

class TestUrl(TestCase):
    def test_home(self):
        url=reverse('speed')
        self.assertEqual(resolve(url).func, speed)