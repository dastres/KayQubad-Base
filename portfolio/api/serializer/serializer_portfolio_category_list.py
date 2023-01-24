from rest_framework import serializers
from portfolio.models.model_portfolio_category import PortfolioCategory
from portfolio.api.serializer.serializer_base_category import BaseCategorySerializer


class CategoryListSerializer(serializers.ModelSerializer):
    categories = BaseCategorySerializer()

    class Meta:
        model = PortfolioCategory
        fields = ['id', 'title', 'slug', 'categories', 'thumbnail', 'thumbnail_alt', 'get_created_at', 'get_updated_at',
                  'status', 'is_active']
        read_only_fields = ['id', 'author', 'get_created_at', 'get_updated_at']
