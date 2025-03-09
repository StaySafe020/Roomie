from django.shortcuts import render

# Create your views here
from rest_framework import viewsets
from .models import Landlord, Tenant, Property, Rental
from .serializers import LandlordSerializer, TenantSerializer, PropertySerializer, RentalSerializer
from django.shortcuts import render, redirect
from .forms import SignupForm



def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Create either a Landlord or Tenant based on the role
            if user.role == 'landlord':
                Landlord.objects.create(user=user)
            elif user.role == 'tenant':
                Tenant.objects.create(user=user)

            return redirect('login')  # Redirect to login or another page
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

class LandlordViewSet(viewsets.ModelViewSet):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer