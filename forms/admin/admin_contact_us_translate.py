# Core Django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# My App
from forms.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', "name", 'email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('id', 'name', 'email', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('Fa'), {'fields': ('name_fa', 'message_fa', 'is_active_fa')}),
        (_('En'), {'fields': ('name_en', 'message_en', 'is_active_en')}),
        (_('Main'), {'fields': ('email', 'phone_number')}),
        (_("Date"), {'fields': ('created_at', "updated_at")}),
    )

    add_fieldsets = (
        (_('Fa'), {'fields': ('name_fa', 'message_fa', 'is_active_fa')}),
        (_('En'), {'fields': ('name_en', 'message_en', 'is_active_en')}),
        (_('Main'), {'fields': ('email', 'phone_number')}),
    )