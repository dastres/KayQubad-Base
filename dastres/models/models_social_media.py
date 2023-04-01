from django.db import models
from django.utils.translation import gettext_lazy as _

from dastres.models import About
from utils.general.models import DateBasic, Status, LanguageStatus


class SocialMedia(DateBasic, Status, LanguageStatus):
    class Meta:
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Media')

    title = models.CharField(_('title'), max_length=200)
    url = models.URLField(_('URL'))
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='socials',
                              verbose_name=_('social media'))

    def __str__(self):
        return self.title
