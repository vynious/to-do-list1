from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= [
            'id',
            'email',
            'first_name',
            'last_name',
        ]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'email',
            'first_name',
            'last_name',
            'password',
        ]
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],validated_data['first_name'],validated_data['last_name'],validated_data['password'])
        return user
        