from django.contrib import admin
from rest_framework.authtoken.models import Token

# Register your models here.



@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')