from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import FileViewset, FileObjectViewset,WorkViewset
from django.conf.urls import include


router = DefaultRouter()
router.register(r'', FileViewset, )
router.register('(?P<file_id>\d+)', FileObjectViewset, )
router.register('(?P<file_id>\d+)/works', WorkViewset, basename='works')
router.register('(?P<file_id>\d+)/works/(?P<work_id>\d+)', WorkViewset, basename='works-detail')
# router.register(r'<int:file_id>/', FileObjectViewset, )

urlpatterns = router.urls
# router.register('files', FileViewset)

# urlpatterns = [
#     path('/', FileViewset, name='files_list'),
#     path('<int:file_id>/', FileObjectViewset,  name='file_detail'),
# ]
# urlpatterns = router.urls

# urlpatterns = [
#     url(r'^$', FileViewset, name='users'),
#     url(r'^(?P<pk>\d+)$', FileObjectViewset, name='user'),
# ]