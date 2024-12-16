# throttling.py
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class CustomUserRateThrottle(UserRateThrottle):
    rate = '100/hour'  # Rate limit for authenticated users

class CustomAnonRateThrottle(AnonRateThrottle):
    rate = '100/hour'  # Rate limit for unauthenticated users