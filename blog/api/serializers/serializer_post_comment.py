from rest_framework import serializers

from blog.models.model_blog_post_comment import PostComment
from blog.api.serializers import BaseCommentSerializer, BasePostSerializer


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            'id','name', 'email', 'message', 'reply', 'is_active', 'status', 'get_like', 'get_dislike'
        )

