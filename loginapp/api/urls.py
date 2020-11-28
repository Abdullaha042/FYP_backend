from xml.etree.ElementInclude import include

from rest_framework.routers import DefaultRouter

from ..views import testingPage, userAuthenticationViewSet

router = DefaultRouter()
router.register(r'',userAuthenticationViewSet,basename='authentication')
urlpatterns = router.urls



#from django.conf.urls import url
#from ..views import testingPage

#urlpatterns = [
#    url(r'^signup/$', testingPage, name='signup'),
#]