from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from utils.general.models import DateBasic, Status, Seo, LanguageStatus, BasicPost
from utils.unique_slug_generator import unique_slug_generator


class Service(DateBasic, Seo, Status, LanguageStatus, BasicPost):
    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    class PositionChoices(models.TextChoices):
        LEFT = _('Left')
        RIGHT = _('Right')

    short_description = RichTextUploadingField(_('Short Description'))
    position = models.CharField(_('Position'), choices=PositionChoices.choices, max_length=5,
                                default=PositionChoices.LEFT)
    is_landing = models.BooleanField(_('is Landing ?'), default=False)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Service)
def pre_post_service_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = unique_slug_generator(instance)
