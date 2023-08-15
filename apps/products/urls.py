from rest_framework import routers

from apps.products.views import ProductsViewSet, WishlistViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'products', ProductsViewSet, basename='products')
router.register(r'wishlists', WishlistViewSet, basename='wishlists')

urlpatterns = [
    *router.urls,
]
