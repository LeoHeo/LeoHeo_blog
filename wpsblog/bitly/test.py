from django.test import TestCase
from bitly.models import BitLink
from django.contrib.auth.models import User


class BitlyTestCase(TestCase):

    def test_bitly_should_have_shorten_hash(self):
        # Create test user
        test_orginal_url = "http://www.naver.com"
        test_username = "test_username"
        test_password = "test_password"
        test_user = User.objects.create_user(
            username=test_username,
            password=test_password
        )

        # create test bitlink
        test_origin_url = "http://www.example.com"
        bitlink = BitLink.objects.create(
            user=test_user,
            origin_url=test_origin_url
        )

        self.assertTrue(
            bitlink.shorten_hash
        )
