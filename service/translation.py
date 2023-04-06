from modeltranslation.translator import register, TranslationOptions
from service.models import Service


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = (
        'title', 'content', 'short_description','is_active','meta_title','meta_description'
    )
