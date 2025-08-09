from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializer import ArticleSerializer
from rest_framework import status
from django.db.models import Q



class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')



class ArticleList(APIView):
    def get(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)




class ArticleAdd(APIView):
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get(self, request, pk):
        try:
            article = Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return Response({"error": "Article not found"}, status=404)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)




class ArticleUpdate(APIView):
    def put(self, request, pk):
        try:
            article = Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ArticleDelete(APIView):
    def delete(self, request, pk):
        try:
            article = Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)

        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class ArticleFilter(APIView):
    def get(self, request, term):
        queryset = Article.objects.filter(
            Q(title__icontains=term) | Q(content__icontains=term) | Q(category__icontains=term)
        )
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

