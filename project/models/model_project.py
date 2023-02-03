# Core Django
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _

# My App
from utils.general.models.model_seo_abstract import Seo
from utils.unique_slug_generator import unique_slug_generator
from utils.general.models.model_status_abstract import Status
from utils.general.models.model_date_abstract import DateBasic
from utils.general.models.model_basic_post_abstract import BasicPost
from utils.general.models.model_language_status_abstract import LanguageStatus
from project.models.model_project_category import ProjectCategory


# ----------------------------------------------------------------------------------------------------------------------


class Project(Seo, BasicPost, DateBasic, Status, LanguageStatus):
    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Project)
def base_post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = unique_slug_generator(instance)
