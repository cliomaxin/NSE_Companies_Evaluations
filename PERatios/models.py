from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class PE_Data(models.Model):
    company_name = models.CharField(max_length=50, default='', blank=True, null=True)
    current_share_price = models.DecimalField(max_digits=5, decimal_places=2, default='', blank=True, null=True)
    earnings_per_share = models.DecimalField(max_digits=5, decimal_places=2, default='', blank=True, null=True)
    highest_earnings_per_share = models.DecimalField(max_digits=5, decimal_places=2, default='', blank=True, null=True)

    def __str__(self):
        return self.company_name or 'Unnamed Company'