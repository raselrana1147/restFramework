
from django.urls import path,include
from RestApp import serializers, views
from rest_framework.routers import  DefaultRouter

router=DefaultRouter()
router.register('article', views.GenericModelArticleViewSet, basename='article')

app_name='rest'

urlpatterns = [
    # functions besed serializers
    # path('article_list/', views.home, name='home_page'),
    # path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),
    
    # class based serializers
    #  path('article_list/', views.ArticleListView.as_view(), name='home_page'),
    #  path('article_detail/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    
    # generic based seriallizer
    
    #  path('article_list/', views.GenericsArticleApiView.as_view(), name='home_page'),
    #  path('article_list/<int:id>/', views.GenericsArticleApiView.as_view(), name='article_detail'),
      # viesets based seriallizer
     path('viewsets/', include(router.urls) ),
     path('viewsets/<int:int>/', include(router.urls) ),
    
]
