from django.urls import path
from .views import (
    get_all_articles_view,
    get_article_view,
    create_article_view,
    update_article_view,
    delete_article_view,

    get_all_products_view,
    get_product_view,
    create_product_view,
    update_product_view,
    delete_product_view,

    get_all_text_view,
    get_text_view,
    create_text_view,
    update_text_view,
    delete_text_view
)

urlpatterns = [
    path('get-all-articles/', get_all_articles_view, name='get-all-articles'),
    path('get-article/<int:pk>/', get_article_view, name='get-article'),
    path('create-article/', create_article_view, name='create-article'),
    path('update-article/<int:pk>/', update_article_view, name='update-article'),
    path('delete-article/<int:pk>/', delete_article_view, name='delete-article'),

    path('get-all-products/', get_all_products_view, name='get-all-products'),
    path('get-product/<int:pk>/', get_product_view, name='get-product'),
    path('create-product/', create_product_view, name='create-product'),
    path('update-product/<int:pk>/', update_product_view, name='update-product'),
    path('delete-product/<int:pk>/', delete_product_view, name='delete-product'),

    path('get-all-text/', get_all_text_view, name='get-all-text'),
    path('get-text/<int:pk>/', get_text_view, name='get-text'),
    path('create-text/', create_text_view, name='create-text'),
    path('update-text/<int:pk>/', update_text_view, name='update-text'),
    path('delete-text/<int:pk>/', delete_text_view, name='delete-text'),
]
