from django.urls import path

from .views import index, article_01

urlpatterns = [
    path('', index, name="blog-index"),
    path('article_01/', article_01, name="blog-article_01"),
]
