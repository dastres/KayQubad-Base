from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.general.models import LanguageStatus


class TeamMembers(LanguageStatus):
    class Meta:
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')

    name = models.CharField(_('name'), max_length=200)
    position = models.CharField(_('position'), max_length=200)
    avatar = models.ImageField(_('avatar'),blank=True,null=True,
                               upload_to=f'dastres/about/avatar/{str(datetime.now().year)}/{str(datetime.now().month)}')


    def __str__(self):
        return self.name
