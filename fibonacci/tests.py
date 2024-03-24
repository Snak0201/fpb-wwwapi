# from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from urllib.parse import urlencode


# Create your tests here.

class FibonacciAPITestCase(APITestCase):
  
  def test_request_with_valid_params_returns_correct_value(self):
    path = "".join([reverse('sampleapp:send_mail'),'?',urlencode(dict(n=10))])
    response = self.client.get(reverse('sampleapp:send_mail'), {"n": 10})
    self.assertEqual(response.status_code, 200)
    expected_json_dict = {
        "value": 55
    }
    self.assertJSONEqual(response.content, expected_json_dict)
