from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

from utils.general.models.model_date_abstract import DateBasic
from utils.general.models.model_status_abstract import Status

from datetime import datetime

class Customers(DateBasic, Status):
    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    name = models.CharField(_('Customer Name'), max_length=350)
    logo = models.ImageField(_('Customer Logo'),
                                  upload_to=f'customer/logo/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                  blank=True, null=True)

    def __str__(self):
        return self.name

    def logo_tag(self):
        return mark_safe('<img src="customer/logo/%s" width="150" height="150" />' % (self.logo))

    logo_tag.short_description = 'Image'