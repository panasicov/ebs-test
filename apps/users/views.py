from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from apps.users.serializers import UserSerializer

user = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
