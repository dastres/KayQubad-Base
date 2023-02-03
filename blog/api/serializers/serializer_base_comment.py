from rest_framework import serializers

from blog.models.model_blog_post_comment import PostComment


class BaseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            'id', 'name', 'email', 'message'
        )
