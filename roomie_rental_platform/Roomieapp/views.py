
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from .models import User
from .serializers import UserSerializer
from rest_framework import permissions

from .exceptions import  CustomAPIException

# Custom permission class
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

# User Registration View
class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            token, _ = Token.objects.create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        
        # Raise a custom exception if the serializer is invalid
        raise CustomAPIException("User registration failed due to invalid data.")

# User Login View
class UserLoginView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if username is None or password is None:
            raise CustomAPIException("Please provide both username and password.")
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise CustomAPIException("Invalid credentials.")
        
        login(request, user)
        token, _ = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)