from django.test import TestCase

class URLTests(TestCase):
    def test_root_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_search_url(self):
        response = self.client.get('/products/search/')
        self.assertEqual(response.status_code, 200)

    def test_cart_url(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_order_create_url(self):
        response = self.client.get('/orders/create/')
        self.assertEqual(response.status_code, 200)

