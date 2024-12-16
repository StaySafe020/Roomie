
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status'] = response.status_code
        response.data['error'] = str(exc)

    return response



class CustomAPIException(APIException):
    status_code = 400
    default_detail = 'A custom error message'
    default_code = 'custom_error'