from django.contrib import admin
from portfolio.models.model_portfolio_gallery import PortfolioGallery


class PortfolioGalleryInline(admin.TabularInline):
    model = PortfolioGallery
    extra = 1
