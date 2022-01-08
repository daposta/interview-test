from rest_framework import serializers
from .models import File, Work

class FileSerializer(serializers.ModelSerializer):
  class Meta:
    model = File
    fields = ('id','filename','work_count')


class WorkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Work
    fields = ('id', 'proprietary_id', 'iswc', 'source', 'title' , 'contributors')