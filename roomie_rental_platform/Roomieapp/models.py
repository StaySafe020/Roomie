from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

# Create your models here.
#This class handles user creation and other user-related functionalities.
class UserManager(BaseUserManager):
    def create_user(self, email, passsword=None, username=None, usertype=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            usertype=usertype,
            )
        user.set_password(passsword)
        user.save()
        return user
    
    def create_superuser(self, email, username, password=None,  **extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)

        if extrafields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extrafields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, username, password, **extrafields)
    

    #Defining the Custom User Model:
#This class represents a user in the system and inherits from AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, blank=True)
    USER_TYPE_CHOICES =(
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='tenant')
    is_staff = models.BooleanField(default='False')
    is_active = models.BooleanField(default='True')

    USERNAME_FIELD = 'email',
    REQUIRED_FIELDS= []

    objects = UserManager()
    def __str__(self):
        return self.email
    

    #property management models
class property(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    images = models.ImageField()
    number_of_rooms = models.PositiveIntegerField()
    amenities = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=225)
    available_status = models.BooleanField(default=True)
    landlord = models.ForeignKey(User,on_delete=models.CASCADE, related_name='properties')


    def __str__(self):
        return self.title


