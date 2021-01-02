from xml.etree.ElementInclude import include
from rest_framework.routers import DefaultRouter
from .views import postStaffViewSet,staffAttributesViewSet,thingAttributesViewSet,departmentAttributesViewSet,postAttributesViewSet

router = DefaultRouter()
router.register(r'addentity',postStaffViewSet,basename='addentities')
router.register(r'attributes',postAttributesViewSet,basename='allattributes')
router.register(r'attributes_staff',staffAttributesViewSet,basename='staff')
router.register(r'attributes_thing',thingAttributesViewSet,basename='thing')
router.register(r'attributes_department',departmentAttributesViewSet,basename='department')

urlpatterns = router.urls