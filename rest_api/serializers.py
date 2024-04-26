from rest_framework import serializers
from .models import ArticleModel, ProductModel, TextModel

# ARTICLE SERIALIZERS
class EditArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ['title', 'content', 'banner']

class GetArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = '__all__'


# PRODUCT SERIALIZERS
class GetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

class EditProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['title', 'image']


# TEXT SERIALIZERS
class GetTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextModel
        fields = '__all__'

class EditTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextModel
        fields = ['title', 'identifier']