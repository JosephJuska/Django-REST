from django.urls import path
from .views import search_view, add_view, control_view

urlpatterns = [
    path('search/', search_view, name='search'),
    path('add/', add_view, name='add'),
    path('control/<int:pk>/', control_view, name='control'),
]
