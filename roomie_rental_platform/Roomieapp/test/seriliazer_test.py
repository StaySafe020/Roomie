import pytest
from rest_framework.exceptions import ValidationError
from django.core.files.base import ContentFile
from Roomieapp.models import User, Property
from Roomieapp.serializers import UserSerializer, PropertySerializer, UserRegistrationSerializer, UserLoginSerializer

@pytest.mark.django_db
def test_user_serializer_create():
    data = {
        'username': 'testuser123',  # Ensure a unique username
        'email': 'testuser@example.com',
        'password': 'testpassword',
        'usertype': 'tenant'
    }
    serializer = UserSerializer(data=data)
    
    assert serializer.is_valid(), serializer.errors  # Check validity
    user = serializer.save()
    
    assert user.username == data['username']
    assert user.email == data['email']
    assert user.check_password(data['password'])
    assert user.usertype == data['usertype']


@pytest.mark.django_db
def test_user_serializer_update():
    user = User.objects.create_user(
        username='existinguser',
        email='existinguser@example.com',
        password='oldpassword',
        usertype='landlord'
    )
    
    data = {
        'email': 'newemail@example.com',
        'usertype': 'tenant',
        'password': 'newpassword'
    }
    serializer = UserSerializer(user, data=data, partial=True)
    assert serializer.is_valid(), serializer.errors  # Print validation errors
    
    updated_user = serializer.save()
    
    assert updated_user.email == data['email']
    assert updated_user.usertype == data['usertype']
    assert updated_user.check_password(data['password'])


@pytest.mark.django_db
def test_property_serializer_create():
    user = User.objects.create_user(
        username='landlord123',  # Ensure unique landlord
        email='landlord@example.com',
        password='landlordpassword',
        usertype='landlord'
    )