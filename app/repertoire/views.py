from django.shortcuts import render
from rest_framework import viewsets
from .models import File, Work
from .serializers import FileSerializer, WorkSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class FileViewset(viewsets.ViewSet):
  """ File resource. """
  queryset = File.objects.all()
  serializer_class = FileSerializer
  

  def list(self, request):
    """
        Return a list of files.

    """
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)
  

class FileObjectViewset(viewsets.ViewSet):
  """ File resource. """
  queryset = File.objects.all()
  serializer_class = FileSerializer

  def list(self, request,file_id):
    """
      Return details of a file by File ID.

    """
    try:
      file_obj = File.objects.get(id =file_id)
    except ObjectDoesNotExist:
      file_obj= {}
    
    serializer = FileSerializer(file_obj)
    return Response(serializer.data)


class WorkViewset(viewsets.ViewSet):
  serializer_class = WorkSerializer
  queryset = Work.objects.all()

  def list(self, request,file_id):
    """
        Return a list of works in a file.

    """
    works = Work.objects.filter(file_id = file_id)
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)


class WorkObjectViewset(viewsets.ViewSet):
  serializer_class = WorkSerializer
  queryset = Work.objects.all()

  def list(self, request, file_id, work_id):
    """
        Return work in a file by ID.

    """
    work = Work.objects.get(file_id = file_id, pk = work_id )
    
    serializer = WorkSerializer(work)
    return Response(serializer.data)