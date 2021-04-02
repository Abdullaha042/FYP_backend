from xml.etree.ElementInclude import include
from rest_framework.routers import DefaultRouter
from .views import postProcessViewSet

router = DefaultRouter()
router.register(r'addprocess',postProcessViewSet,basename='addentities')

urlpatterns = router.urls