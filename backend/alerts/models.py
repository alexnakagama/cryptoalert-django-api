from django.db import models

from django.contrib.auth.models import User

from cryptos.models import Crypto

# Create your models here.

CONDITION_CHOICES = [
    ('above', 'Above'), ('below', 'Below')
]

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    
    target_price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=10)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    triggered_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user}, {self.crypto}, {self.condition}"
    

STATUS_CHOICES = [
    ('sent', 'Sent'), ('failed', 'Failed')
]

class AlertNotification(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    price_at_trigger = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    notified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.alert}, {self.price_at_trigger}$, {self.status}"