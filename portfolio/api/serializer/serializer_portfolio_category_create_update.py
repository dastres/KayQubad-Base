from rest_framework import serializers
from portfolio.models.model_portfolio_category import PortfolioCategory


class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = ['meta_title', 'meta_description', 'title', 'description', 'slug', 'categories', 'thumbnail',
                  'thumbnail_alt', 'sub_category', 'status', 'is_active']

