from modeltranslation.translator import register, TranslationOptions
from portfolio.models import Portfolio, PortfolioCategory


@register(PortfolioCategory)
class PortfolioCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'is_active', 'sub_category','meta_title','meta_description')


@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'is_active', 'category','meta_title','meta_description')