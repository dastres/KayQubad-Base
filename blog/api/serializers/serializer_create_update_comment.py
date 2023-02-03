from rest_framework import serializers

from blog.models.model_blog_post_comment import PostComment


class CreateUpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            'name', 'email', 'message', 'reply', 'post', 'is_active', 'status'
        )