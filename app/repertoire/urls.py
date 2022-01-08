from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import FileViewset
from django.conf.urls import include

router = DefaultRouter()
router.register('files', FileViewset, base_name='files')
# router.register('files', FileViewset)

urlpatterns = [
    path('', include(router.urls))
    #get list of files
    #get files by id
    #Returns a list of works defined in a file
    #Returns a list of works defined in a file.
]
