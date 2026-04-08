from rest_framework import routers

from .views import CryptoViewSet, CryptoFavoriteViewSet, CryptoPriceHistoryViewSet, CurrencyViewSet

router = routers.DefaultRouter()

router.register(r'cryptos', CryptoViewSet)
router.register(r'favorites', CryptoFavoriteViewSet)
router.register(r'price-history', CryptoPriceHistoryViewSet)
router.register(r'currencies', CurrencyViewSet)

urlpatterns = router.urls