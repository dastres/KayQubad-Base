from django.contrib import admin
from portfolio.models.model_portfolio import Portfolio
from portfolio.admin.admin_inline_portfolio_gallery import PortfolioGalleryInline


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioGalleryInline, ]
    list_display = ('title', 'author', 'slug', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'slug', 'category')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Main', {'fields': ('title', 'author', 'content', 'slug', 'category',)}),
        ("Seo information", {'fields': ("meta_title", "meta_description")}),
        ('Date', {'classes': ('collapse',), 'fields': ('created_at', 'updated_at')})
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'author', 'content', 'slug', 'category',)}),
        ("Seo information", {'fields': ("meta_title", "meta_description")}),
    )
