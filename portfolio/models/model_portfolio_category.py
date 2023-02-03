from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from utils.general.models.model_seo_abstract import Seo
from utils.general.models.model_date_abstract import DateBasic
from utils.general.models.model_taxonomy_abstraction import Taxonomy
from utils.general.models.model_status_abstract import Status
from utils.general.models.model_language_status_abstract import LanguageStatus
from utils.unique_slug_generator import unique_slug_generator


class PortfolioCategory(Seo, DateBasic, Taxonomy, Status, LanguageStatus):
    class Meta:
        verbose_name = _('Portfolio Category')
        verbose_name_plural = _('Portfolios Categories')

    sub_category = models.ForeignKey('self', models.CASCADE, related_name='categories', blank=True, null=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=PortfolioCategory)
def pre_portfolio_category_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = unique_slug_generator(instance)
