from rest_framework import serializers

from apps.products.models import Product, Wishlist


class ProductSerializer(serializers.ModelSerializer):
    wishlist_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ['wishlists']

    def get_wishlist_count(self, obj):
        return obj.wishlists.values('user').distinct().count()


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        exclude = ['user']

    def save(self, **kwargs):
        self.validated_data['user'] = self.context['request'].user
        return super().save(**kwargs)


class WishlistDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Wishlist
        exclude = ['user']


class ProductWishlistSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()