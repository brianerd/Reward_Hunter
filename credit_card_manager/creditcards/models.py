from django.db import models

# Create your models here.
class CreditCards(models.Model):
  bank_name = models.CharField(max_length=255)
  card_name = models.CharField(max_length=255)