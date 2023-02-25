from rest_framework import serializers
from marketing.models import UserComment


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = (
            'name', 'company', 'avatar', 'avatar_alt', 'content', 'rate', 'is_active', 'get_created_at',
            'get_updated_at'
        )
        read_only_fields = ('id', 'get_updated_at', 'get_created_at')
