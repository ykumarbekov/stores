from django.db import models


class Customer(models.Model):
    customerid = models.IntegerField(default=0)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    creditcard = models.CharField(max_length=255)
    income = models.IntegerField()
    age = models.SmallIntegerField()
    gender = models.CharField(max_length=1)
    orderid = models.IntegerField()
    orderdate = models.DateField()
    totalamount = models.DecimalField(max_digits=12, decimal_places=2)