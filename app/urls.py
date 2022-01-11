from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Files API')
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', schema_view),
    path('api/', include('repertoire.urls')),
     
    

   
]
