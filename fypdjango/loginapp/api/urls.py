from xml.etree.ElementInclude import include

from rest_framework.routers import DefaultRouter

from ..views import userAuthenticationViewSet,postViewSet

router = DefaultRouter()
router.register(r'post',postViewSet,basename='post')
router.register(r'',userAuthenticationViewSet,basename='authentication')

urlpatterns = router.urls