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

    def validate_rate(self, value):
        if value.rate in [0, 2, 3, 4, 5]:
            return value
        raise serializers.ValidationError("Invalid rate")
