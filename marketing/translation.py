from modeltranslation.translator import register, TranslationOptions
from marketing.models import UserComment


@register(UserComment)
class UserCommentTranslationOptions(TranslationOptions):
    fields = ('name', 'company', 'content', 'is_active')
