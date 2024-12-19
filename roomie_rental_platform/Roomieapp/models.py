from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User 
from .models import User


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, usertype='tenant', **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, usertype=usertype, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """Create and return a superuser with an email, username, and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('usertype', 'landlord')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractUser):
    """Custom User model that extends AbstractUser."""
    USER_TYPE_CHOICES = (
        ('tenant', 'Tenant'),
        ('landlord', 'Landlord'),
    )

    usertype = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='tenant')
    email = models.EmailField(unique=True)  # Ensure unique email addresses

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Ensure username must be provided when creating a user

    objects = UserManager()

    def __str__(self):
        return self.email

# Property management models
class Property(models.Model):
    """Model representing a property managed by a landlord."""
    title = models.CharField(max_length=225)
    description = models.TextField()
    images = models.ImageField(upload_to='property_images/')
    number_of_rooms = models.PositiveIntegerField()
    amenities = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=225)
    available_status = models.BooleanField(default=True)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')

    def __str__(self):
        return self.title
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username