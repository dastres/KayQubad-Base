from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from dastres.models import TeamMembers
from dastres.admin import SocialMediaInline


@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position')
    list_filter = ('position',)
    search_fields = ('id', 'name', 'position')
    inlines = [SocialMediaInline, ]

    fieldsets = (
        (_("Main_en"), {'fields': ('name_en', 'position_en', 'is_active_en')}),
        (_("Main_fa"), {'fields': ('name_fa', 'position_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('avatar',)}),
    )
