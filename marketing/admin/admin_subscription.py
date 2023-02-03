# Core Django
from django.contrib import admin

# My App
from marketing.models import EmailSubscription

@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at', 'updated_at')
    search_fields = ('id', 'email', 'created_at', 'updated_at')