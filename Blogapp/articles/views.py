from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the article model.
    """
    queryset = Article.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = ArticleSerializer

    #adding the custom permission
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)