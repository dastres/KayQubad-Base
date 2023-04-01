from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from dastres.models import SocialMedia


class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 0

    fieldsets = (
        (_("Main_en"), {'fields': ('title_en', 'is_active_en', 'status_en')}),
        (_("Main_fa"), {'fields': ('title_fa', 'is_active_fa', 'status_fa')}),
        (_("Main"), {'fields': ('url', 'about')}),
    )
