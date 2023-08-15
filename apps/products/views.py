from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.products.models import Product, Wishlist
from apps.products.serializers import (
    ProductSerializer,
    WishlistSerializer,
    ProductWishlistSerializer,
    WishlistDetailSerializer,
)


class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class WishlistViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return WishlistDetailSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['post'], serializer_class=ProductWishlistSerializer)
    def add_product(self, request, pk=None):
        wishlist = self.get_object()
        product = Product.objects.get(id=request.data['product_id'])
        wishlist.products.add(product)
        return Response(WishlistSerializer(wishlist).data)

    @action(detail=True, methods=['post'], serializer_class=ProductWishlistSerializer)
    def remove_product(self, request, pk=None):
        wishlist = self.get_object()
        product = Product.objects.get(id=request.data['product_id'])
        wishlist.products.remove(product)
        return Response(WishlistSerializer(wishlist).data)
