from rest_framework import serializers
from dastres.models.models_landing_sections import LandingSections


class LandingToAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingSections
        fields = (
            "title_one",
            "count_one",
            "title_two",
            "count_two",
            "title_three",
            "count_three",
        )

