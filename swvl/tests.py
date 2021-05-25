from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from setuptools.command.egg_info import egg_info

from swvl.models import Captin
from swvl.views import CreateCaptin


class CaptinTest(APITestCase):

    def setUp(self):
        # url = reverse("create_captin")
        # print(url)
        # data = {"phone_number": "010010656", "email": "samir_mohamed@gmail.com"}
        # response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertTrue('id' in response.data, '')
        Captin.objects.create(phone_number='1001065536', email='amr@gmail.com')

    def test_captin(self):
        cation = Captin.objects.get(email='amr@gmail.com')
        self.assertEqual("Casper belongs to Bull Dog breed.")
