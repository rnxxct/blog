# 引入path
from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
     path('article-list/', views.article_list, name='article_list'),
     path('article-index/', views.article_index, name='article_index'),
     path('article-index/cloud10.png', views.article_index_png, name='article_index_png'),
     path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
     path('article-create/', views.article_create, name='article_create'),
     path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
     path('article-update/<int:id>/', views.article_update, name='article_update'),
]