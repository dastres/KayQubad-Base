from rest_framework import serializers

from blog.models.model_blog_post_comment import PostComment
from blog.api.serializers import BaseCommentSerializer, BasePostSerializer


class ListCommentSerializer(serializers.ModelSerializer):
    post = BasePostSerializer()
    reply = serializers.SerializerMethodField(method_name='get_reply')

    class Meta:
        model = PostComment
        fields = (
            'name', 'email','message', 'reply', 'post', 'is_active', 'status'
        )

    def get_reply(self, obj):
        result = obj.post_comments.all()
        serializer = BaseCommentSerializer(result, many=True)
        return serializer.data
