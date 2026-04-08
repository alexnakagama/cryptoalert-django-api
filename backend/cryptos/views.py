from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Crypto, CryptoFavorite, CryptoPriceHistory, Currency
from .serializers import CryptoSerializer, CryptoFavoriteSerializer, CryptoPriceHistorySerializer, CurrencySerializer

# Create your views here.

class CryptoViewSet(viewsets.ModelViewSet):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer
    
class CryptoFavoriteViewSet(viewsets.ModelViewSet):
    queryset = CryptoFavorite.objects.all()
    serializer_class = CryptoFavoriteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return CryptoFavorite.objects.filter(user=user)
    
class CryptoPriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = CryptoPriceHistory.objects.all()
    serializer_class = CryptoPriceHistorySerializer
    
class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer