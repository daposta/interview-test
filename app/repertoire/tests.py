# from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from repertoire.models import File, Work

# Create your tests here.
class FilesAPITestcase(APITestCase):

    
  def test_lists(self):
    response = self.client.get('/files/')
    print(response)
    #self.assertEqual(type(response), [])
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_file_detail(self):
    file_obj = File.objects.create(filename = 'Test')
    
    contributor_list = 'Kanye West|Da Baby'.split('|')
    work_obj = Work.objects.create(title = 'Donda', contributors= contributor_list, iswc = 'dd8902834', 
            source = 'Warner', proprietary_id = 4, file_id = file_obj )
    
    response = self.client.get(f'/files/{file_obj.id}/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    

  def test_works_in_file(self):
    file_obj = File.objects.create(filename = 'Test1')
    
    contributor_list = 'Kanye West|Da Baby'.split('|')
    work_obj = Work.objects.create(title = 'Donda', contributors= contributor_list, iswc = 'dd8902834', 
            source = 'Warner', proprietary_id = 4, file_id = file_obj )
    
    response = self.client.get(f'/files/{file_obj.id}/works/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_work_in_file(self):
    file_obj = File.objects.create(filename = 'Test2')
    
    contributor_list = 'Kanye West|Da Baby'.split('|')
    work_obj = Work.objects.create(title = 'Donda', contributors= contributor_list, iswc = 'dd8902834', 
            source = 'Rockafella', proprietary_id = 4, file_id = file_obj )
    
    response = self.client.get(f'/files/{file_obj.id}/works/{work_obj.id}/')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['source'], 'Rockafella')
    
