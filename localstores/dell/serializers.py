from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customerid',
                  'firstname',
                  'lastname',
                  'city',
                  'country',
                  'phone',
                  'creditcard',
                  'income',
                  'age',
                  'gender',
                  'orderid',
                  'orderdate',
                  'totalamount']
