from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from utils.general.models.model_date_abstract import DateBasic


class BaseComment(DateBasic):
    class Meta:
        abstract = True

    name = models.CharField(_('name'), max_length=350)
    email = models.EmailField(_('email'))
    message = RichTextUploadingField(_('message'))
