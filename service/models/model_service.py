from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from utils.general.models import DateBasic, Status, Seo, LanguageStatus, BasicPost


class Service(DateBasic, Seo, Status, LanguageStatus, BasicPost):
    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    class PositionChoices(models.TextChoices):
        LEFT = 'Left'
        RIGHT = 'Right'

    short_description = RichTextUploadingField(_('Short Description'))
    position = models.CharField(_('Position'), choices=PositionChoices.choices, max_length=5,
                                default=PositionChoices.LEFT)
    is_landing = models.BooleanField(_('is Landing ?'), default=False)

    def __str__(self):
        return self.title
