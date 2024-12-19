
from rest_framework.exceptions import APIException

class CustomAPIException(APIException):
    status_code = 400
    default_detail = 'A server error occured'
    default_code = 'error'