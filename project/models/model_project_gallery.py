# Core Django
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

# My App
from project.models.model_project import Project

from utils.general.models.model_status_abstract import Status
from utils.general.models.model_date_abstract import DateBasic
from utils.general.models.model_basic_gallery_abstract import BasicGallery


# ----------------------------------------------------------------------------------------------------------------------
class ProjectGallery(BasicGallery, DateBasic, Status):
    class Meta:
        verbose_name = _('Project Gallery')
        verbose_name_plural = _('Project Gallery')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_gallery')

    def __str__(self):
        return self.project.title

    def save(self, *args, **kwargs):
        self.image_alt = slugify(self.title)
        super().save(*args, **kwargs)