from django.urls import path

from accounts import views


urlpatterns = [
    path('create/', views.UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', views.UserLoginAPIView.as_view(), name='user-login'),
    path('', views.UserListAPIView.as_view(), name='user-list'),
    path('me/', views.ManageUserView.as_view(), name='user-detail')
]

