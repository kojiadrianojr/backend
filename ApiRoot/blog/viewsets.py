from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from blog.models import Blog
from blog.serializers import BlogSerializer

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer
  permission_classes = [AllowAny]

