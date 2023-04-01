from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.general.models import Seo, LanguageStatus
from ckeditor.fields import RichTextField


class About(Seo, LanguageStatus):
    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')

    cover_video = models.ImageField(_('Cover Video'),blank=True,null=True,
                                    upload_to=f'about/cover_video/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                    )
    video = models.FileField(_('Video'),blank=True,null=True,
                             upload_to=f'about/video/{str(datetime.now().year)}/{str(datetime.now().month)}',
                             )
    description = RichTextField(_('Description'))

    def __str__(self):
        return self.pk

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValidationError(_('There is can be only one About instance'))
        return super().save(*args, **kwargs)
