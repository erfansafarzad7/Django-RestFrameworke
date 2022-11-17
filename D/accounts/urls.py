from django.urls import path
from . import views
from rest_framework.authtoken import views as token_auth

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('api-token-auth/', token_auth.obtain_auth_token),
]
