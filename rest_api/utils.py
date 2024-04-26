from rest_framework.response import Response
from rest_framework import status

def method_is_valid(request, method):
    return request.method == method
    
def respond_method_not_valid():
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={'error':'Method not allowed'})
    
def respond_not_found(data_type):
    return Response(status=status.HTTP_404_NOT_FOUND, data={'error':f'{data_type} not found'})

def respond_no_data_provided():
    return Response(status=status.HTTP_400_NOT_FOUND, data={'error':'No data provided'})