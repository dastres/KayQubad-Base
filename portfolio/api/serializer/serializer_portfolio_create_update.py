from rest_framework import serializers

from portfolio.api.serializer.serializer_portfolio_category_list import CategoryListSerializer
from portfolio.models.model_portfolio import Portfolio


class PortfolioCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = [
            'title', 'content', 'category', 'slug', 'thumbnail', 'thumbnail_alt', 'status', 'is_active',
        ]
