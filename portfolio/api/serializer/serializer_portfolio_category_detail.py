from rest_framework import serializers
from portfolio.models.model_portfolio_category import PortfolioCategory
from portfolio.api.serializer.serializer_base_category import BaseCategorySerializer


class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_category = BaseCategorySerializer()

    class Meta:
        model = PortfolioCategory
        fields = ['id', 'meta_title', 'meta_description', 'title', 'description', 'slug', 'categories', 'thumbnail',
                  'thumbnail_alt', 'sub_category', "get_created_at", "get_updated_at", 'status', 'is_active']
        read_only_fields = ['id', 'author', 'get_created_at', 'get_updated_at']
