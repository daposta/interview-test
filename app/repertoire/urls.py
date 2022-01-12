from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import FileViewset, FileObjectViewset,WorkViewset, WorkObjectViewset
from django.conf.urls import include


router = DefaultRouter()
router.register(r'', FileViewset, )
router.register('(?P<file_id>\d+)', FileObjectViewset, )
router.register('(?P<file_id>\d+)/works', WorkViewset, basename='works')
router.register('(?P<file_id>\d+)/works/(?P<work_id>\d+)', WorkObjectViewset, basename='works-detail')


urlpatterns = router.urls
