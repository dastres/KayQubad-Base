from rest_framework import serializers
from dastres.models import About
from dastres.api.serializer.serializer_base_social_media import SocialMediaBaseSerializer


class AboutListDetailSerializer(serializers.ModelSerializer):
    socials = SocialMediaBaseSerializer(many=True)

    class Meta:
        model = About
        fields = (
            'id', 'name', 'position', 'avatar', 'socials', 'is_active'
        )
