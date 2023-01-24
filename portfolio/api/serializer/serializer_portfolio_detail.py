from rest_framework import serializers

from accounts.api.serializers import BaseUserSerializer
from portfolio.models.model_portfolio import Portfolio
from portfolio.api.serializer.serializer_base_category import BaseCategorySerializer


class PortfolioDetailSerializer(serializers.ModelSerializer):
    author = BaseUserSerializer()
    category = BaseCategorySerializer()

    class Meta:
        model = Portfolio
        fields = [
            'id', 'title', 'content', 'category', 'author', 'slug', 'thumbnail', 'thumbnail_alt', 'get_created_at',
            'get_updated_at', 'status', 'is_active',
        ]
        read_only_fields = ['id', 'author', 'get_created_at', 'get_updated_at']
