from django.db import models

# Create your models here.

class Crypto(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, unique=True)
    image = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=100)
    
    current_price = models.DecimalField(max_digits=10, decimal_places=10)
    market_cap = models.DecimalField(max_digits=30, decimal_places=2)
    market_cap_rank = models.PositiveIntegerField(null=True, blank=True)
    
    price_change_24h = models.DecimalField(max_digits=20, decimal_places=8, null=True, blank=True)
    price_change_percentage_24h = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.symbol})"
    
class CryptoPriceHistory(models.Model):
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_length=20, decimal_places=8)
    price_24h = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        unique_together = ('crypto', 'timestamp')