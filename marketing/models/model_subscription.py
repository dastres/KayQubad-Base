from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.general.models.model_date_abstract import DateBasic

class EmailSubscription(DateBasic):
    class Meta:
        verbose_name = _('Email Subscription')
        verbose_name_plural = _('Email Subscriptions')


    email = models.EmailField(_("Email Subscription"), max_length=254)