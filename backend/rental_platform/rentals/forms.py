
from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)