from random import choices
from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from services.get_pokemons_service import get_pokemons


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user register"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
                'min_length': 8
            }}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provide credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    """User profile serializer with all fields"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
