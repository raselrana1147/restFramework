from os import stat
from django.shortcuts import get_object_or_404, render
from RestApp import serializers
from RestApp.models import Article
from RestApp.serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer


class ArticleListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article.html'
    
    def get(self, request):
        articles=Article.objects.all().order_by('-id')
        serializer=ArticleSerializer(articles,many=True)
        return Response({'articles':articles})
    
    def post(self, request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( {'message':'Successfully added','status':status.HTTP_201_CREATED})


class ArticleDetailView(APIView):
    def get_objects(self,pk):
        try:
            # return get_object_or_404(Article,id=pk)
            return Article.objects.get(id=pk)
        except Article.DoesNotExists:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        article=self.get_objects(pk)
        serializer=ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        article=self.get_objects(pk)
        serializer=ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Successfully updated',"status":status.HTTP_202_ACCEPTED})
        else:
            return Response({'message':'Something went wrong',"status":status.HTTP_400_BAD_REQUEST})
    def delete(self, request,pk):
        self.get_objects(pk).delete()
        return Response({'message':'Successfully deleted',"status":status.HTTP_200_OK})
        
    
        
            
        
    
    
    
    
""" 
# Create your views here.
@api_view(['GET', 'POST'])
def home(request):
    if request.method=="GET":
        article=Article.objects.all().order_by('-id')
        serializer=ArticleSerializer(article, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        # data=JSONParser().parse(request)
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        artcle=Article.objects.get(id=pk)
    except artcle.DoesNotExists:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer=ArticleSerializer(artcle)
        return Response(serializer.data)
    if request.method == 'PUT':
        
        serializer=ArticleSerializer(artcle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        artcle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
        
"""