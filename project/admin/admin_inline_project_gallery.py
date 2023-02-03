# Core Django
from django.contrib import admin

# My APP
from project.models.model_project_gallery import ProjectGallery


# ----------------------------------------------------------------------------------------------------------------------

class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 1
