from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    ###path('adduser/',include('loginapp.api.urls')),

    #Signup endpoint
    path('api/user/', include('users.urls',namespace='users')),#signin credentials hit here
    #Signin endpoint
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#this endpoint will allow us to generate tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    #Posting Entities
    path('entity/', include(('entities.urls', 'entities'), namespace='entities')),

    #Processes
    path('process/', include(('processes.urls', 'processes'), namespace='processes')),

    #Reset Passwords
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view() ,name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view() ,name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view() ,name='password_reset_complete'),

]