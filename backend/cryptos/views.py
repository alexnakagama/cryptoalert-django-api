from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Crypto, CryptoFavorite, CryptoPriceHistory, Currency
from .serializers import CryptoSerializer, CryptoFavoriteSerializer, CryptoPriceHistorySerializer, CurrencySerializer

from .services import get_crypto_price, get_max_price, get_min_price

# Create your views here.

class CryptoYaListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        currency = request.query_params.get('currency', 'ARS')
        volume = request.query_params.get('volume', '0.01')
        
        # You can add more
        symbols = ['BTC', 'ETH', 'USDT', 'XRP', 'USDC', 'DAI', 'BNB', 'SOL', 'ADA', 'TRX', 'DOGE', 'SHIB', 'XLM', 'LINK']
        logos = {
            'BTC': 'https://cryptologos.cc/logos/bitcoin-btc-logo.png',
            'ETH': 'https://cryptologos.cc/logos/ethereum-eth-logo.png',
            'USDT': 'https://cryptologos.cc/logos/tether-usdt-logo.png',
            'XRP': 'https://cryptologos.cc/logos/xrp-xrp-logo.png',
            'USDC': 'https://cryptologos.cc/logos/usd-coin-usdc-logo.png',
            'DAI': 'https://cryptologos.cc/logos/multi-collateral-dai-dai-logo.png',
            'BNB': 'https://cryptologos.cc/logos/binance-coin-bnb-logo.png',
            'SOL': 'https://cryptologos.cc/logos/solana-sol-logo.png',
            'ADA': 'https://cryptologos.cc/logos/cardano-ada-logo.png',
            'TRX': 'https://cryptologos.cc/logos/tron-trx-logo.png',
            'DOGE': 'https://cryptologos.cc/logos/dogecoin-doge-logo.png',
            'SHIB': 'https://cryptologos.cc/logos/shiba-inu-shib-logo.png',
            'XLM': 'https://cryptologos.cc/logos/stellar-xlm-logo.png',
            'LINK': 'https://cryptologos.cc/logos/chainlink-link-logo.png',
        }
        names = {
            'BTC': 'Bitcoin',
            'ETH': 'Ethereum',
            'USDT': 'Tether',
            'XRP': 'XRP',
            'USDC': 'USD Coin',
            'DAI': 'Dai',
            'BNB': 'Binance Coin',
            'SOL': 'Solana',
            'ADA': 'Cardano',
            'TRX': 'Tron',
            'DOGE': 'Dogecoin',
            'SHIB': 'Shiba Inu',
            'XLM': 'Stellar',
            'LINK': 'Chainlink',
        }
        result = []
        
        for symbol in symbols:
            min_price = get_min_price(symbol, currency, volume)
            max_price = get_max_price(symbol, currency, volume)
            result.append({
                'symbol': symbol,
                'name': names[symbol],
                'min_price': min_price,
                'max_price': max_price,
                'logo': logos[symbol],
            })
        return Response(result)
    
class CryptoViewSet(viewsets.ModelViewSet):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer
    permission_classes = [AllowAny]
    
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