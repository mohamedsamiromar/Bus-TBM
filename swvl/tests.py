from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from swvl.models import Bus, Trip, Captin


class UserLoginTestCase(APITestCase):

    def setUp_captin(self):
        user = User(username="omar", email="omar@gmail.com", first_name="omar", last_name="amr")
        user.set_password('201040mo')
        self.user = user.save()
        token = Token.objects.create(user=user)
        self.token = token.key
        print('sign in')

    def test_create_account(self):
        print(self.token)
        url = reverse('register')
        data = {"username": "testcase", "email": "testcase@gmail.com",
                "password": "testcase", "first_name": "testcase", "last_name": "testcase"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print('create new account')

    def test_login(self):
        url = reverse('api_token_auth')
        data = {"username": "omar", "password": "201040mo"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('login')

    def test_bus(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        url = reverse('bus')
        data = {"bus_number": "15029", "color_bus": "red", "number_seat": 14, "model_bus": "2011"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        bus_number = response.data.get('bus_number')
        bus = Bus.objects.get(bus_number=bus_number)
        self.assertEqual(bus.bus_number, bus_number)
        print('create bus')

    # def test_captin(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    #     url = reverse('create_captin')
    #     data = {"user": "1", "phone_number": "01001065536", "email": "samir@gmail.com"}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     print('create captin')
    #
    # def test_trip(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    #     url = reverse('trip')
    #     data = {"bus": "1", "from_address": "tanta", "to_address": "basun", "captin": "1", "from_data": "02:00:00 AM",
    #             "to_data": "03:00:00 PM", "price": 6, "reserved": 14}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     print('create trip')
