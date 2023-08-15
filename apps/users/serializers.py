from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


user_model = get_user_model()


class UserSerializer(ModelSerializer):

    class Meta:
        model = user_model
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = user_model.objects.create_user(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
