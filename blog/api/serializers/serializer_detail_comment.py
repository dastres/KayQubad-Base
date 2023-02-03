
from rest_framework import serializers

from blog.models.model_blog_post_comment import PostComment
from blog.api.serializers.serializer_base_comment import BaseCommentSerializer
from blog.api.serializers.serializer_base_post import BasePostSerializer


class DetailCommentSerializer(serializers.ModelSerializer):
    reply = BaseCommentSerializer()
    post = BasePostSerializer()

    class Meta:
        model = PostComment
        fields = (
            'id', 'name', 'email', 'message', 'reply', 'post', 'is_active', 'status', 'get_created_at', 'get_updated_at'
        )