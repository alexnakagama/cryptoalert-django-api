# Convert the models to JSON

from rest_framework import serializers

from .models import Crypto, CryptoPriceHistory, CryptoFavorite, Currency

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = [
            'id',
            'name',
            'symbol',
            'image',
            'description',
            'current_price',
            'market_cap',
            'market_cap_rank',
            'price_change_24h',
            'price_change_percentage_24h',
            'last_updated',
        ]
        
class CryptoPriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoPriceHistory
        fields = [
            'id',
            'crypto',
            'price',
            'price_24h',
            'timestamp',
        ]
        
class CryptoFavoriteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CryptoFavorite
        fields = [
            'id',
            'user',
            'crypto',
            'added_at',
        ]
        
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'id',
            'code',
            'name',
        ]