from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'password','confirm_password')
        read_only_fields = ('id',)

    def validate_username(self, value):
        """
            This function checks that the username does not exist in the database
        """
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError(_("The user exists with this username."))
        return value

    def validate_email(self, value):
        """
            This function checks that the email does not exist in the database
        """
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError(_("The user exists with this email."))
        return value

    def validate(self, data):
        """ This function checks if the password is equal to confirm password"""
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(_("The password does not match the confirm password."))
        return data

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password')
        user = get_user_model().objects.create(**validated_data)
        return user
