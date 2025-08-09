from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializer import ArticleSerializer



class ArticleList(APIView):
    def get(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)



class ArticleAdd(APIView):
    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"added"})
        return Response(serializer.errors)



class ArticleDetail(APIView):
    def post(self,request, pk):
        queryset = Article.objects.get(id=pk)
        serializer = ArticleSerializer(queryset)
        return Response(serializer.data)

