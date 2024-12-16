from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Property

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'usertype')
        read_only_fields = ('id', 'username')
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
        read_only_fields = ('id','available_status','price')

        class UserRegistrationSerializer(serializers.ModelSerializer):
         password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_type', 'password')
        extra_kwargs = {'password': {'write_only': True}}  # Hide password in response

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')