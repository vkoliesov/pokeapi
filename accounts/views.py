from django.contrib.auth import get_user_model

from rest_framework import permissions, authentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from accounts import serializers


class UserRegisterAPIView(CreateAPIView):
    """Register a new user"""
    serializer_class = serializers.UserSerializer


class UserLoginAPIView(ObtainAuthToken):
    """Login registered users"""
    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserListAPIView(ListAPIView):
    """Users list"""
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class ManageUserView(RetrieveUpdateAPIView):
    """Managed authenticated user"""
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrive and return authentication user"""
        return self.request.user

