from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author/<int:pk>', views.author, name = 'get_author'),
    path('author', views.authorlist, name = 'author'),
    path('article/<int:pk>', views.article, name = 'get_article'),
    path('create_article', views.create_article, name = 'create_article'),
    path('create_author', views.create_author, name = 'create_author')
]