from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import path, include, reverse
from rest_framework import status
import json
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate

from . models import Customer


class DellCustomersApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('tester', '123456789')
        self.client.force_authenticate(self.user)
    #     ******************
        Customer.objects.create(
            customerid=1, firstname='xxx', lastname='yyy', age=36, gender='M',
            city='DHHPRLW',
            country='US',
            phone='5353378339',
            creditcard='5026723033282906',
            income=60000,
            orderid=8498,
            orderdate='2004-09-10',
            totalamount=157.04
        )

    #     ******************

    def test_customers_res(self):
        res = self.client.get('/dell/customers?ordering=orderdate&country=US')
        data = json.loads(res.content.decode('utf-8'))
        self.assertEqual(len(data), 1)

    def test_url(self):
        res = self.client.get(reverse('customers'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

