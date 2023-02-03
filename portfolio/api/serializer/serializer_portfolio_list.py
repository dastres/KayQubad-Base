from rest_framework import serializers
from portfolio.models.model_portfolio import Portfolio
from portfolio.api.serializer.serializer_base_category import BaseCategorySerializer


class PortfolioListSerializer(serializers.ModelSerializer):
    category = BaseCategorySerializer()

    class Meta:
        model = Portfolio
        fields = (
            'id', 'title', 'category', 'get_created_at', 'get_updated_at', 'slug', 'thumbnail', 'thumbnail_alt'
        )
        read_only_fields = ['id', 'get_created_at', 'get_updated_at']
