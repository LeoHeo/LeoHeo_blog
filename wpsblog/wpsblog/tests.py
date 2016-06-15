from django.test import TestCase
from django.core.urlresolvers import reverse


class HomeViewTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse("home"))

    def test_home_view_should_return_200(self):
        self.assertEqual(
            self.response.status_code,
            200
        )
