from rest_framework import serializers

from blog.models.model_blog_post_comment import PostComment


class BaseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            'name', 'email','message', 'is_active', 'status','get_like', 'get_dislike'
        )
