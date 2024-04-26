from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ArticleModel, ProductModel, TextModel
from .serializers import (
    GetArticleSerializer, 
    EditArticleSerializer,

    GetProductSerializer, 
    EditProductSerializer,

    GetTextSerializer,
    EditTextSerializer)

from .utils import (
    method_is_valid,
    respond_method_not_valid,
    respond_no_data_provided,
    respond_not_found
    )

# Create your views here.

# ARTICLE VIEWS
@api_view(['GET'])
def get_all_articles_view(request):
    if not method_is_valid(request, 'GET'):
        return respond_method_not_valid()
    
    queryset = ArticleModel.objects.all()

    if queryset.exists():
        serializer = GetArticleSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data={'data':serializer.data})
    
    return respond_not_found('Article')

@api_view(['GET'])
def get_article_view(request, pk):
    if not method_is_valid(request, 'GET'):
        return respond_method_not_valid()
    
    try:
        instance = ArticleModel.objects.get(pk=pk)
        serializer = GetArticleSerializer(instance=instance)

    except ArticleModel.DoesNotExist:
        return respond_not_found('Article')
    
    return Response(status=status.HTTP_200_OK, data={'data':serializer.data})

@api_view(['POST'])
def create_article_view(request):
    if not method_is_valid(request, 'POST'):
        return respond_method_not_valid()
     
    data = request.data
    if not data:
        return respond_no_data_provided()
     
    serializer = EditArticleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data={'data':serializer.data})

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
    
@api_view(['PUT'])
def update_article_view(request, pk):
    if not method_is_valid(request, 'PUT'):
        return respond_method_not_valid()
    
    try:
        instance = ArticleModel.objects.get(pk=pk)
        data = request.data
        if not data:
            return respond_no_data_provided()

        serializer = EditArticleSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED, data={'data':serializer.data})
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
                            
    except ArticleModel.DoesNotExist:
        return respond_not_found('Article')
    
@api_view(['DELETE'])
def delete_article_view(request, pk):
    if not method_is_valid(request, 'DELETE'):
        return respond_method_not_valid()
    
    try:
        instance = ArticleModel.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except ArticleModel.DoesNotExist:
        return respond_not_found('Article')



# PRODUCT VIEWS
@api_view(['GET'])
def get_all_products_view(request):
    if not (request, 'GET'):
        return respond_method_not_valid()

    queryset = ProductModel.objects.all()
    
    if queryset.exists():
        serializer = GetProductSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer)
    
    return respond_not_found('Product')

@api_view(['GET'])
def get_product_view(request, pk):
    if not method_is_valid(request, 'GET'):
        return respond_method_not_valid()

    try:
        instance = ProductModel.objects.get(pk=pk)
        serializer = GetProductSerializer(instance=instance)
        return Response(status=status.HTTP_200_OK, data=serializer)
    
    except ProductModel.DoesNotExist:
        return respond_not_found('Product')
    
@api_view(['POST'])
def create_product_view(request):
    if not method_is_valid(request, 'POST'):
        return respond_method_not_valid()
     
    data = request.data
    if not data:
        return respond_no_data_provided()
     
    serializer = EditProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data={'data':serializer.data})

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
    
@api_view(['PUT'])
def update_product_view(request, pk):
    if not method_is_valid(request, 'PUT'):
        return respond_method_not_valid()
    
    try:
        instance = ProductModel.objects.get(pk=pk)
        data = request.data
        if not data:
            return respond_no_data_provided()

        serializer = EditProductSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED, data={'data':serializer.data})
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
                            
    except ProductModel.DoesNotExist:
        return respond_not_found('Product')
    
@api_view(['DELETE'])
def delete_product_view(request, pk):
    if not method_is_valid(request, 'DELETE'):
        return respond_method_not_valid()
    
    try:
        instance = ArticleModel.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except ProductModel.DoesNotExist:
        return respond_not_found('Product')


# TEXt VIEWS
@api_view(['GET'])
def get_all_text_view(request):
    method_is_valid(request, 'GET')

    queryset = TextModel.objects.all()
    
    if queryset.exists():
        serializer = GetTextSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer)

    return respond_not_found('Text')

@api_view(['GET'])
def get_text_view(request, pk):
    if not method_is_valid(request, 'GET'):
        return respond_method_not_valid()

    try:
        instance = TextModel.objects.get(pk=pk)
        serializer = GetTextSerializer(instance=instance)
        return Response(status=status.HTTP_200_OK, data=serializer)
    
    except TextModel.DoesNotExist:
        return respond_not_found('Text')
    
@api_view(['POST'])
def create_text_view(request):
    if not method_is_valid(request, 'POST'):
        return respond_method_not_valid()
     
    data = request.data
    if not data:
        return respond_no_data_provided()
     
    serializer = EditTextSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data={'data':serializer.data})

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
    
@api_view(['PUT'])
def update_text_view(request, pk):
    if not method_is_valid(request, 'PUT'):
        return respond_method_not_valid()
    
    try:
        instance = TextModel.objects.get(pk=pk)
        data = request.data
        if not data:
            return respond_no_data_provided()

        serializer = EditTextSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED, data={'data':serializer.data})
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})
                            
    except TextModel.DoesNotExist:
        return respond_not_found('Text')
    
@api_view(['DELETE'])
def delete_text_view(request, pk):
    if not method_is_valid(request, 'DELETE'):
        return respond_method_not_valid()
    
    try:
        instance = TextModel.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except TextModel.DoesNotExist:
        return respond_not_found('Text')