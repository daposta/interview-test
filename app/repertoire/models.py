from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class File(models.Model):
  filename = models.CharField(max_length=30, unique=True)
  work_count = models.IntegerField(default=0)

class Work(models.Model):
  proprietary_id = models.IntegerField()
  iswc = models.CharField(max_length=30)
  source = models.CharField(max_length=30)
  title = models.CharField(max_length=30)
  contributors = ArrayField(models.CharField(max_length=200), blank=True)
  file_id = models.ForeignKey(File, on_delete=models.CASCADE)

  # class Meta:
  #   unique_together = ('title', 'contributors')