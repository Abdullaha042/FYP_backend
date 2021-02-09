from xml.etree.ElementInclude import include
from rest_framework.routers import DefaultRouter
from .views import postStaffViewSet,staffAttributesViewSet,thingAttributesViewSet,departmentAttributesViewSet,postAttributesViewSet,allStaffMembersViewSet,allThingsViewSet,allDepartmentsViewSet,allEntityConfiguration,staffEntityConfiguration,thingEntityConfiguration,departmentEntityConfiguration

router = DefaultRouter()
router.register(r'addentity',postStaffViewSet,basename='addentities')
router.register(r'attributes',postAttributesViewSet,basename='allattributes')

router.register(r'get_staff',allStaffMembersViewSet,basename='staff')
router.register(r'attributes_staff',staffAttributesViewSet,basename='staff')
router.register(r'attributes_thing',thingAttributesViewSet,basename='thing')
router.register(r'attributes_department',departmentAttributesViewSet,basename='department')

router.register(r'get_thing',allThingsViewSet,basename='department')
router.register(r'get_department',allDepartmentsViewSet,basename='department')

#Entity Configuration
router.register(r'configuration',allEntityConfiguration,basename='entity_configuration')
router.register(r'get_conf_staff',staffEntityConfiguration,basename='entity_configurationStaff')
router.register(r'get_conf_thing',thingEntityConfiguration,basename='entity_configurationThing')
router.register(r'get_conf_department',departmentEntityConfiguration,basename='entity_configurationDepartment')


urlpatterns = router.urls