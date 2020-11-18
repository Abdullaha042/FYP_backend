from xml.etree.ElementInclude import include

from rest_framework.routers import DefaultRouter

from ..views import testingPage, AuthenticationGoogleViewSet

router = DefaultRouter()
router.register(r'',AuthenticationGoogleViewSet,basename='authentication')
urlpatterns = router.urls



#from django.conf.urls import url
#from ..views import testingPage

#urlpatterns = [

#    url(r'^signup/$', testingPage, name='signup'),
#]