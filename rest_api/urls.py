from django.urls import path
from .views import (
    get_all_articles_view,
    get_article_with_id_view,
    create_article_view,
    update_article_view,
    delete_article_view
)

urlpatterns = [
    path('get-all-articles/', get_all_articles_view, name='get-all-articles'),
    path('get-article/<int:pk>/', get_article_with_id_view, name='get-article'),
    path('create-article/', create_article_view, name='create-article'),
    path('update-article/<int:pk>/', update_article_view, name='update-article'),
    path('delete-article/<int:pk>/', delete_article_view, name='delete-article'),
]
