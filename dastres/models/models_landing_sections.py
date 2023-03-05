from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.general.models import DateBasic, Seo, Status, LanguageStatus


class LandingSections(DateBasic, Status, LanguageStatus):
    class Meta:
        verbose_name = _('Landing Section')
        verbose_name_plural = _('Landing Sections')

    # Slider
    cover_main = models.ImageField(_('Cover Main'),
                                   upload_to=f'landing_sections/cover_main/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                   )
    title_main_one = models.CharField(_('Title Main One'), max_length=100)
    title_main_two = models.CharField(_('Title Main Two'), max_length=100)

    # About
    title_small = models.CharField(_('Title Small'), max_length=100)
    title_big = models.CharField(_('Title Big'), max_length=350)
    short_description = models.TextField(_('Short Description'))
    link = models.URLField(_('Link'))
    cover_background = models.ImageField(_('Cover Background'),
                                         upload_to=f'landing_sections/cover_background/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                         )
    cover_video = models.ImageField(_('Cover Video'),
                                    upload_to=f'landing_sections/cover_video/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                    )
    link_video = models.URLField(_('Link Video'))

    title_one = models.CharField(_('Title One'), max_length=100)
    count_one = models.CharField(_('Count One'), max_length=100)

    title_two = models.CharField(_('Title Two'), max_length=100)
    count_two = models.CharField(_('Count Two'), max_length=100)

    title_three = models.CharField(_('Title Three'), max_length=100)
    count_three = models.CharField(_('Count Three'), max_length=100)

    def __str__(self):
        return self.title_main_one
