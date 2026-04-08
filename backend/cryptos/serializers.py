# Convert the models to JSON

from rest_framework import serializers

from .models import Crypto, CryptoPriceHistory, CryptoFavorite, Currency

from .services import get_min_price, get_max_price

class CryptoSerializer(serializers.ModelSerializer):
    
    min_price = serializers.SerializerMethodField()
    max_price = serializers.SerializerMethodField()
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
            'min_price',
            'max_price',
        ]
        
    def get_min_price(self, obj):
        return get_min_price(obj.symbol, "ARS", "0.01")
        
    def get_max_price(self, obj):
        return get_max_price(obj.symbol, "ARS", "0.01")    
    
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