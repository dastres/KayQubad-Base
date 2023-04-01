from modeltranslation.translator import register, TranslationOptions
from dastres.models import LandingSections, SocialMedia, About


@register(LandingSections)
class LandingSectionsTranslationOptions(TranslationOptions):
    fields = (
        'title_main_one',
        'title_main_two',
        'title_small',
        'title_big',
        'short_description',
        'title_one',
        'count_one',
        'title_two',
        'count_two',
        'title_three',
        'count_three',
        'is_active',
    )


@register(SocialMedia)
class SocialMediaTranslationOptions(TranslationOptions):
    fields = ('title', 'is_active', 'status')


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'is_active')
