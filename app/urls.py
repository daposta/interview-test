from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework_swagger.views import get_swagger_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_swagger_view(title='Files API', )

urlpatterns = [
   
    path('', schema_view),
    path('files/', include('repertoire.urls')),
    
   
]
