from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from dastres.models import LandingSections


@admin.register(LandingSections)
class LandingSectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_main_one', "title_main_two", 'status', 'created_at', 'updated_at', 'is_active')
    search_fields = (
        'id', 'title_main_one', 'title_main_two', 'title_small', 'title_big', 'title_one', 'title_two', 'title_three'
    )
    list_filter = ('status', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('En'),
         {'fields': ('title_main_one_en', 'title_main_two_en', 'title_small_en', 'title_big_en', 'short_description_en',
                     'title_one_en', 'title_two_en', 'title_three_en', 'is_active_en')}),
        (_('Fa'),
         {'fields': ('title_main_one_fa', 'title_main_two_fa', 'title_small_fa', 'title_big_fa', 'short_description_fa',
                     'title_one_fa', 'title_two_fa', 'title_three_fa', 'is_active_fa')}),

        (_("Main"), {'fields': (
        'cover_main', 'link', 'cover_background', 'cover_video', 'link_video', 'count_one', 'count_two',
        'count_three')}),
        (_("Setting"), {'fields': ("status",)}),
        (_("Date"), {'fields': ("created_at",'updated_at')}),
    )


    add_fieldsets = (
        (_('En'),
         {'fields': ('title_main_one_en', 'title_main_two_en', 'title_small_en', 'title_big_en', 'short_description_en',
                     'title_one_en', 'title_two_en', 'title_three_en', 'is_active_en')}),
        (_('Fa'),
         {'fields': ('title_main_one_fa', 'title_main_two_fa', 'title_small_fa', 'title_big_fa', 'short_description_fa',
                     'title_one_fa', 'title_two_fa', 'title_three_fa', 'is_active_fa')}),

        (_("Main"), {'fields': (
        'cover_main', 'link', 'cover_background', 'cover_video', 'link_video', 'count_one', 'count_two',
        'count_three')}),
        (_("Setting"), {'fields': ("status",)}),
        (_("Date"), {'fields': ("created_at",'updated_at')}),
    )
