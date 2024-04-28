from rest_framework import  serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = ['id', 'owner', 'title', 'description']
    read_only_fields = ['created', 'updated', 'id']