from rest_framework import serializers

from dastres.models.models_customers import Customers


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id','name','logo']
