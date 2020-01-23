from django.urls import path
from article.views import list_article, detail_article, create_article, create_comment

urlpatterns = [
    path('', list_article, name='list-article'),
    path('<int:pk>/', detail_article, name='detail-article'),
    path('create/', create_article, name='create-article'),
    path('create/<int:pk>/', create_comment, name='create-comment'),
]