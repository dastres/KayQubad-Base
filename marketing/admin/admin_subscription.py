# Core Django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# My App
from marketing.models import EmailSubscription

@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at', 'updated_at')
    search_fields = ('id', 'email', 'created_at', 'updated_at')