from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from dastres.models import About
from dastres.admin import SocialMediaInline


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

    fieldsets = (
        (_("Main_en"), {'fields': ('description_en', 'is_active_en')}),
        (_("Main_fa"), {'fields': ('description_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('cover_video', 'video')}),
        (_("Seo"), {'fields': ('meta_title', 'meta_description')}),
    )
