from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from blog.models import Blog
from blog.serializers import BlogSerializer

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

