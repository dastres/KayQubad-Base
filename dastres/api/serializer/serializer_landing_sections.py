from rest_framework import serializers

from dastres.models import LandingSections


class LandingSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingSections
        fields = (
            'cover_main',
            'title_main_one',
            'title_main_two',
            'title_small',
            'title_big',
            'short_description',
            'link',
            'cover_background',
            'cover_video',
            'link_video',
            'title_one',
            'count_one',
            'title_two',
            'count_two',
            'title_three',
            'count_three',
        )
