from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from portfolio.models.model_portfolio import Portfolio
from portfolio.admin.admin_inline_portfolio_gallery import PortfolioGalleryInline


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioGalleryInline, ]
    list_display = ('id', 'title', 'author', 'slug', 'category', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'author', 'slug', 'category')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('En'), {'fields': ('title_en', 'content_en', 'category_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'content_fa', 'category_fa', 'is_active_fa')}),
        (_('Main'), {'fields': ('author', 'slug', 'thumbnail', 'thumbnail_alt')}),
        (_("Seo information"), {'fields': ("meta_title", "meta_description")}),
        (_('Date'), {'classes': ('collapse',), 'fields': ('created_at', 'updated_at')}),
        (_('Setting'), {'classes': ('collapse',), 'fields': ('status',)})
    )

    add_fieldsets = (
        (_('En'), {'fields': ('title_en', 'content_en', 'category_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'content_fa', 'category_fa', 'is_active_fa')}),
        (_('Main'), {'fields': ('author', 'slug', 'thumbnail', 'thumbnail_alt')}),
        (_("Seo information"), {'fields': ("meta_title", "meta_description")}),
        (_('Setting'), {'classes': ('collapse',), 'fields': ('status',)})
    )