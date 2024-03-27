from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q
from .models import TestModel1, TestModel2
from .serializers import SearchSerializer1, SearchSerializer2, PostSerializer1

# Create your views here.

'''
Function - search_view
Preview - Takes search value from request and returns a list of results depending on the provided fields.
Parameters:
request - The request object
Inside Parameters:
fields - List of tuples which contains model and a list of fields. For example: [(TestModel, ['name', 'surname']), (BookModel, ['author'])].
Change it accordingly to get desired results.
'''
@api_view(['GET'])
def search_view(request) -> Response:
    search_value = request.GET.get('search-value', '')
    if not search_value:
        return Response(data={'error':'Search value not provided'}, status=status.HTTP_404_NOT_FOUND)
    
    fields = [
        (TestModel1, ['name', 'surname']),
        (TestModel2, ['header']),
    ]
    
    result = []
    for model, field_list in fields:
        q_objects = Q()
        for field in field_list:
            if hasattr(model, field):
                q_objects |= Q(**{f'{field}__icontains' : search_value})
            else:
                raise KeyError(f'{model} has no such field: {field}')
        
        queryset = model.objects.filter(q_objects)

        if model == TestModel1:
            serializer = SearchSerializer1(queryset, many=True)
            result.extend(serializer.data)

        elif model == TestModel2:
            serializer = SearchSerializer2(queryset, many=True)
            result.extend(serializer.data)

        response = {'data' : result}

    return Response(data=response, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_view(request):
    if request.method == 'POST':
        data = request.data
        if not data:
            return Response('No data provided', status=status.HTTP_404_NOT_FOUND)
        
        result = PostSerializer1(data=data)
        if result.is_valid():
            result.save()
            return Response(data={'data':result.data}, status=status.HTTP_201_CREATED)
        
        else:
            return Response(data={'error':result.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response(data={'error':'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['DELETE', 'PUT'])
def control_view(request, pk):
    try:
        instance = TestModel1.objects.get(pk=pk)
    except TestModel1.DoesNotExist:
        return Response(data={'error':'ID does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        instance.delete()
        return Response(data={'data':'success'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        result = PostSerializer1(instance=instance, data=request.data)
        if result.is_valid():
            result.save()
            return Response(data={'data':result.data}, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(data={'error':result.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    else:
        return Response(data={'error':'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)