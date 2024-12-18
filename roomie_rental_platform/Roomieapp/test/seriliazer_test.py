import pytest
from rest_framework.exceptions import ValidationError
from Roomieapp.models import User, Property
from Roomieapp.serializers import UserSerializer, PropertySerializer, UserLoginSerializer

@pytest.mark.django_db
def test_user_serializer_create():
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword',
        'usertype': 'tenant'
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'
    assert user.check_password('testpassword')  # Check password hashing

@pytest.mark.django_db
def test_user_serializer_update():
    user = User.objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='testpassword',
        usertype='tenant'
    )

    data = {
        'email': 'newemail@example.com',
        'usertype': 'landlord',
        'password': 'newpassword'
    }
    serializer = UserSerializer(instance=user, data=data, partial=True)
    assert serializer.is_valid()
    updated_user = serializer.save()
    assert updated_user.email == 'newemail@example.com'
    assert updated_user.user_type == 'landlord'
    assert updated_user.check_password('newpassword')  # Check password hashing

@pytest.mark.django_db
def test_property_serializer_create():
    user = User.objects.create_user(
        username='landlord',
        email='landlord@example.com',
        password='landlordpassword',
        usertype='landlord'
    )

    data = {
        'title': 'Test Property',
        'description': 'A lovely test property.',
        'images': None,  # You can mock this if needed
        'number_of_rooms': 3,
        'amenities': 'Pool, Gym',
        'price': 2500.00,
        'location': '123 Test St, Test City',
        'landlord': user.id  # Use the ID of the created user
    }
    serializer = PropertySerializer(data=data)
    assert serializer.is_valid()
    property_instance = serializer.save()
    assert property_instance.title == 'Test Property'
    assert property_instance.landlord == user

@pytest.mark.django_db
def test_user_login_serializer():
    user = User.objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='testpassword',
        usertype='tenant'
    )

    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    serializer = UserLoginSerializer(data=data)
    assert serializer.is_valid()
    # Optionally, you can simulate a login attempt and ensure it works