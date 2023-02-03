from django.db import models
from django.utils.translation import gettext_lazy as _


class LanguageStatus(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(_('is active'), default=False)