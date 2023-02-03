from rest_framework import serializers

from blog.models.model_blog_post_comment import PostComment
from blog.api.serializers import BaseCommentSerializer, BasePostSerializer


class ListCommentSerializer(serializers.ModelSerializer):
    reply = BaseCommentSerializer()
    post = BasePostSerializer()

    class Meta:
        model = PostComment
        fields = (
            'name', 'email', 'reply', 'post', 'is_active', 'status'
        )
