from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import RichTextUploadingField

from utils.general.models.model_date_abstract import DateBasic
from utils.general.models.model_language_status_abstract import LanguageStatus


class UserComment(DateBasic, LanguageStatus):
    class Meta:
        verbose_name = _('User Comment')
        verbose_name_plural = _('User Comments')

    name = models.CharField(_('name'), max_length=350)
    company = models.CharField(_('company'), max_length=20)
    avatar = models.ImageField(_('avatar'),
                               upload_to=f'marketing/user_comment/user_comment/avatar/{str(datetime.now().year)}/{str(datetime.now().month)}')
    avatar_alt = models.CharField(_('avatar alt'), max_length=350, blank=True)
    rate = models.PositiveSmallIntegerField(_('rate'), default=0)
    content = RichTextUploadingField(_('content'))

    def clean(self):
        if not self.rate in [0, 1, 2, 3, 4, 5]:
            ValidationError(_('The rate must be between 0 and 5'))

        super().clean()

    def save(self, *args, **kwargs):
        if not self.avatar_alt:
            self.avatar_alt = slugify(self.name)
        self.full_clean()
        super().save(*args, **kwargs)
