from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ArticleModel
from .serializers import ArticleSerializer

# Create your views here.
@api_view(['GET'])
def get_article_with_id_view(request, pk):
    if request.method != 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={'error':'Method not allowed'})
    
    try:
        instance = ArticleModel.objects.get(pk=pk)
        serializer = ArticleSerializer(instance=instance)

    except ArticleModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'Article not found'})
    
    return Response(status=status.HTTP_200_OK, data={'data':serializer.data})

@api_view(['GET'])
def get_all_articles_view(request):
    if request.method != 'GET':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={'error':'Method not allowed'})
    
    queryset = ArticleModel.objects.all()

    if not queryset.exists():
         return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'Article not found'})
    
    serializer = ArticleSerializer(queryset, many=True)
    return Response(status=status.HTTP_200_OK, data={'data':serializer.data})

@api_view(['POST'])
def create_article_view(request):
    if request.method != 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={'error':'Method not allowed'})
     
    data = request.data
    if not data:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'No data provided'})
     
    serializer = ArticleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data={'data':serializer.data})

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
    
@api_view(['PUT'])
def update_article_view(request, pk):
    if request.method != 'PUT':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={'error':'Method not allowed'})
    
    try:
        instance = ArticleModel.objects.get(pk=pk)
        data = request.data
        if not data:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'No data provided'})

        serializer = ArticleSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED, data={'data':serializer.data})
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
                            
    except ArticleModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'Article not found'})
    
@api_view(['DELETE'])
def delete_article_view(request, pk):
    if request.method != 'DELETE':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data={'error':'Method not allowed'})
    
    try:
        instance = ArticleModel.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except ArticleModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'Article not found'})