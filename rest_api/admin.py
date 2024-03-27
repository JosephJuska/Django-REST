from django.contrib import admin
from .models import TestModel1, TestModel2
# Register your models here.

class Admin1(admin.ModelAdmin):
    list_display = ('name', 'surname')

class Admin2(admin.ModelAdmin):
    list_display = ('header', 'author')

admin.site.register(TestModel1, Admin1)
admin.site.register(TestModel2, Admin2)