# serializers.py

from rest_framework import serializers
from .models import User, Property

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Use your custom User model
        fields = ('id', 'username', 'email', 'password', 'usertype')
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            usertype=validated_data['usertype']
        )
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.usertype = validated_data.get('usertype', instance.usertype)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'title', 'description', 'images', 'number_of_rooms', 'amenities', 'price', 'location', 'available_status', 'landlord')
        read_only_fields = ('id', 'available_status', 'price')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Use your custom User model
        fields = ('id', 'username', 'email', 'usertype', 'password')
        extra_kwargs = {'password': {'write_only': True}}  # Hide password in response


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Use your custom User model
        fields = ('username', 'password')