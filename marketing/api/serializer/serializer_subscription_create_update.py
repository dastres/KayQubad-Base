from rest_framework import serializers

from marketing.models.model_subscription import EmailSubscription


class EmailSubscriptionCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        fields = ('email')
