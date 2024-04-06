from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.


class FibonacciAPITestCase(APITestCase):
    """api/fibonacci/v1/number"""

    def setUp(self):
        self.url = reverse("fibonacci:number")

    def test_get_with_positive_integer_returns_correct_value(self):
        """nが正の整数のとき、正しい値を取得できる"""
        response = self.client.get(self.url, {"n": 10})
        self.assertEqual(response.status_code, 200)
        expected_json_dict = {"value": 55}
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_get_with_0_returns_correct_value(self):
        """nが0のとき、正しい値を取得できる"""
        response = self.client.get(self.url, {"n": 0})
        self.assertEqual(response.status_code, 200)
        expected_json_dict = {"value": 0}
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_get_with_negative_integer_returns_400_error(self):
        """nが負の整数のとき、エラーとなる"""
        response = self.client.get(self.url, {"n": -1})
        self.assertEqual(response.status_code, 400)
        expected_json_dict = {"value": None, "errors": {"n": ["この値は0以上にしてください。"]}}
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_get_with_float_returns_400_error(self):
        """nが小数を含むとき、エラーとなる"""
        response = self.client.get(self.url, {"n": 0.5})
        self.assertEqual(response.status_code, 400)
        expected_json_dict = {"value": None, "errors": {"n": ["有効な整数を入力してください。"]}}
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_get_with_none_returns_400_error(self):
        """nがないとき、エラーとなる"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)
        expected_json_dict = {"value": None, "errors": {"n": ["この項目はnullにできません。"]}}
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_post_returns_405_error(self):
        """リクエストメソッドがGETでないとき、エラーとなる"""
        response = self.client.post(self.url, {"n": 10})
        self.assertEqual(response.status_code, 405)
        expected_json_dict = {"value": None, "errors": {"detail": 'メソッド "POST" は許されていません。'}}
        self.assertJSONEqual(response.content, expected_json_dict)
