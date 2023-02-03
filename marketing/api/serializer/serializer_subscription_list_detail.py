from rest_framework import serializers

from marketing.models.model_subscription import EmailSubscription


class EmailSubscriptionListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        fields = ('id', 'email', 'created_at', 'updated_at')
