from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from dastres.models.models_social_media import SocialMedia
from utils.general.models import LanguageStatus


class About(LanguageStatus):
    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')

    name = models.CharField(_('name'), max_length=200)
    position = models.CharField(_('position'), max_length=200)
    avatar = models.ImageField(_('avatar'),
                               upload_to=f'dastres/about/avatar/{str(datetime.now().year)}/{str(datetime.now().month)}')
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, related_name='abouts',
                                     verbose_name=_('about'))

    def __str__(self):
        return self.name
