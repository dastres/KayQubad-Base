from django.contrib import admin
from dastres.models import SocialMedia


class SocialMediaInline(admin.StackedInline):
    model = SocialMedia
    extra = 1
