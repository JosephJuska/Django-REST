from rest_framework import serializers
from .models import TestModel1, TestModel2

class SearchSerializer1(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = TestModel1
        fields = '__all__'

    def get_type(self, obj):
        return str(obj)

class SearchSerializer2(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = TestModel2
        fields = '__all__'

    def get_type(self, obj):
        return str(obj)
    
class PostSerializer1(serializers.ModelSerializer):
    class Meta:
        model = TestModel1
        fields = '__all__'