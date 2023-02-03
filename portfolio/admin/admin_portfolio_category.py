from django.contrib import admin
from portfolio.models.model_portfolio_category import PortfolioCategory


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sub_category', 'created_at', 'updated_at')
    search_fields = ('title', 'sub_category', 'slug', 'category')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Seo information", {'fields': ("meta_title", "meta_description")}),
        ('Main', {'fields': ('title', 'slug', 'description', 'sub_category', 'thumbnail', 'thumbnail_alt')}),
        ('Date', {'classes': ('collapse',), 'fields': ('created_at', 'updated_at')})
    )

    add_fieldsets = (
        ("Seo information", {'fields': ("meta_title", "meta_description")}),
        ('Main', {'fields': ('title', 'slug', 'description', 'sub_category', 'thumbnail', 'thumbnail_alt')}),

    )
