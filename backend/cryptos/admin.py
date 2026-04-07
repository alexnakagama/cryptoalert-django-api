from django.contrib import admin

from .models import Crypto, CryptoFavorite, CryptoPriceHistory, Currency

# Register your models here.
admin.site.register(Crypto)
admin.site.register(CryptoPriceHistory)
admin.site.register(CryptoFavorite)
admin.site.register(Currency)