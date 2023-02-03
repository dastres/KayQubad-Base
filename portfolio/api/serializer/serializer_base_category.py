from rest_framework import serializers

from portfolio.models import PortfolioCategory


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = ['id', 'title', 'slug']
        read_only_fields = ['id', 'author', 'get_created_at', 'get_updated_at']