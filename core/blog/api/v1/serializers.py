from rest_framework import serializers
from django.contrib.auth import get_user_model

from blog.models import Post, Category

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'image',
            'title',
            'content',
            'status',
            'published_date',
            'author',
            'category'
        )
        read_only_fields = ('id', 'author')

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        validated_data["author"] = user
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'parent',
        )