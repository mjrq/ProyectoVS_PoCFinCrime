from django.db import models
from django.db.models import Sum
from django.views.generic import ListView
# Create your models here.

class CUSTOMERS(models.Model):
    CUSTOMER_SOURCE_UNIQUE_ID = models.CharField(max_length=100,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
 
class ACCOUNTS(models.Model):
    ACCOUNT_SOURCE_UNIQUE_ID = models.CharField(max_length=100,primary_key=True)
    ACCOUNT_BALANCE = models.DecimalField(max_digits=8,decimal_places=2)

class CUSTOMER_ACOUNT_LINK(models.Model):
    CUSTOMER_SOURCE_UNIQUE_ID=models.ForeignKey(CUSTOMERS,on_delete=models.CASCADE)
    ACCOUNT_SOURCE_UNIQUE_ID=models.ForeignKey(ACCOUNTS,on_delete=models.CASCADE)