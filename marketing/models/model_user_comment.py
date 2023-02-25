from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
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
    avatar = models.ImageField(_('avatar'),blank=True,null=True,
                               upload_to=f'marketing/user_comment/user_comment/avatar/{str(datetime.now().year)}/{str(datetime.now().month)}')
    avatar_alt = models.CharField(_('avatar alt'), max_length=350, blank=True)
    content = RichTextUploadingField(_('content'))
    rate = models.IntegerField(_('rate'), default=0,
                                            validators=[
                                                MaxValueValidator(5),
                                                MinValueValidator(0)
                                            ])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.avatar_alt:
            self.avatar_alt = slugify(self.name)
        super().save(*args, **kwargs)
