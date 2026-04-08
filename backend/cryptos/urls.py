from rest_framework import routers

from django.urls import path

from .views import CryptoYaListView, CryptoFavoriteViewSet, CryptoPriceHistoryViewSet, CurrencyViewSet

router = routers.DefaultRouter()

router.register(r'favorites', CryptoFavoriteViewSet)
router.register(r'price-history', CryptoPriceHistoryViewSet)
router.register(r'currencies', CurrencyViewSet)

urlpatterns = [
    path('cryptos/', CryptoYaListView.as_view())
]

urlpatterns += router.urls