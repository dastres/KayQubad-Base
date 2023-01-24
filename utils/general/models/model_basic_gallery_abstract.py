from django.db import models
from django.utils.translation import gettext_lazy as _

from datetime import datetime


class BasicGallery(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(_('title'), max_length=350)
    image = models.ImageField(_('image'),
                              upload_to=f'basic_gallery/images/{str(datetime.now().year)}/{str(datetime.now().month)}')
    image_alt = models.CharField(_('image alt'), max_length=350, blank=True)
