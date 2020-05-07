from django.db import models
from django.db.models import Sum
# Create your models here.

class Clientes(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
  


class Cuentas(models.Model):
    question = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)