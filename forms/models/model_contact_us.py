from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from utils.general.models.model_date_abstract import DateBasic
from utils.general.models.model_language_status_abstract import LanguageStatus


class ContactUs(DateBasic, LanguageStatus):
    class Meta:
        verbose_name = _('Contact-Us')
        verbose_name_plural = _('Contact-Us')

    class RequiredServices(models.TextChoices):
        DedicatedTranslation = _('DET')
        SimpleTranslation = _('SIT')
        EconomicTranslation = _('ECT')
        SpecialTranslation = _('SPT')

    phone_number_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("The phone number is invalid."))
    name = models.CharField(_('name'), max_length=350)
    email = models.EmailField(_('email'))
    phone_number = models.CharField(_('phone number'), max_length=11, validators=[phone_number_validator])
    message = RichTextUploadingField(_('message'))
    required_services = models.CharField(_('required_services'), max_length=3,
                                         default=RequiredServices.SimpleTranslation,
                                         choices=RequiredServices.choices)

    def __str__(self):
        return self.email
