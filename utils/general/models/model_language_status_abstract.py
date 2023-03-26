from django.db import models
from django.utils.translation import gettext_lazy as _


class LanguageStatus(models.Model):
    class Meta:
        abstract = True

    class IsActiveChoices(models.IntegerChoices):
        ACTIVE = 1, _('ACTIVE')
        INACTIVE = 0, _('INACTIVE')

    is_active = models.IntegerField(_('is active ?'), choices=IsActiveChoices.choices, default=IsActiveChoices.INACTIVE)
