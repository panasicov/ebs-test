from rest_framework import routers

from apps.users.views import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    *router.urls,
]
