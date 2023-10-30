from django.db import models

# Create your models here.
class CreditCards(models.Model):
  bank_name = models.CharField(max_length=255)
  card_name = models.CharField(max_length=255)
  
  def __str__(self):
      return f"{self.bank_name} {self.card_name}"
    
  

