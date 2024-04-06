from django.urls import reverse
from rest_framework.test import APITestCase

class SimpleDiceAPITestCase(APITestCase):
    """api/dice/v1/simple"""

    def test_post_100_times_returns_correct_values(self):
        """APIから値を100回取得したとき、全ての値が正しい範囲である"""
        for _ in range(100):
            response = self.client.post(reverse("dice:simple"))
            self.assertGreaterEqual(response.data["value"], 1)
            self.assertLessEqual(response.data["value"], 6)
        self.assertEqual(response.status_code, 201)
