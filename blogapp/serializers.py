from rest_framework import serializers
from django.contrib.auth.models import User
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'author',
            'category',
            'content',
            'excerpt',
            'image',
            'tags',
            'created_at',
            'updated_at',
            'status',
            'views',
            'is_featured',
        ]
