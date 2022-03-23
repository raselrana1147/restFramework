
from django.urls import path
from RestApp import views
app_name='rest'
urlpatterns = [
    # path('article_list/', views.home, name='home_page'),
    # path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),
    
     path('article_list/', views.ArticleListView.as_view(), name='home_page'),
     path('article_detail/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
