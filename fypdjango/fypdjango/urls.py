from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    #path('adduser/',include('loginapp.api.urls')),
    path('api/user/',include('users.urls',namespace='users')),#login credentials hit here

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#this endpoint will allow us to generate tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]