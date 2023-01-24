from rest_framework import serializers
from blog.models.model_blog_post_comment import PostComment


class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'
