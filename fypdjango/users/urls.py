from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CustomUserCreate,BlacklistTokenUpdateView,CustomUserRetrieve

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),#signup view
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),name='blacklist'),
]

router = DefaultRouter()
router.register(r'getauthusers',CustomUserRetrieve,basename='get_user')

urlpatterns = router.urls