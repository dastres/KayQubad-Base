# Core Django
from django.contrib import admin

# My App
from dastres.models import Customers

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo_tag', 'created_at', 'updated_at')
    search_fields = ('id', 'name', 'created_at', 'updated_at')