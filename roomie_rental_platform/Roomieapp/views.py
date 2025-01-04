from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods, action
import json
from django.http import JsonResponse
from .serializers import UserLoginSerializer, UserSerializer, UserProfileSerializer, PropertySerializer
from .models import User, UserProfile, Property, Inquiry
from rest_framework import permissions
from django.contrib.auth import get_user_model


# Custom permission class
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

# User Registration View
class UserRegistrationView(APIView):
    def post(self, request):
        try:
            data = request.data
            User = get_user_model()

            # Validate required fields
            required_fields = ['email', 'password', 'full_name', 'usertype']
            for field in required_fields:
                if not data.get(field):
                    return Response(
                        {'message': f'{field} is required'}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
            # Check if user already exists
            if User.objects.filter(email=data['email']).exists():
                return Response(
                    {'message': 'User with this email already exists'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Create user
            user = User.objects.create_user(
                username=data['email'],
                email=data['email'],
                password=data['password'],
                usertype=data['usertype']
            )

            # Create user profile
            profile_data = {
                'user': user,
                'phone': data.get('phone', ''),
            }
            if data['usertype'] == 'tenant':
                profile_data['location'] = data.get('location', '')
            else:
                profile_data['company_name'] = data.get('company_name', '')
                profile_data['business_address'] = data.get('location', '')

            UserProfile.objects.create(**profile_data)

            # Return success response
            return Response({
                'message': 'Registration successful',
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# User Login View
class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        usertype = request.data.get('usertype')

        if not email or not password:
            return Response({
                'message': 'Please provide both email and password'
            }, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if user and user.usertype == usertype:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'usertype': user.usertype
                }
            }, status=status.HTTP_200_OK)
        
        return Response({
            'message': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)

# User Profile ViewSet
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Property List and Create ViewSet
class PropertyDetailViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)