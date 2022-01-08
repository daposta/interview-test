# from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class FilesAPITestcase(APITestCase):

    
  def test_lists(self):
    url = reverse('files')
    response = self.client.get(url, format='json')
    print(response.data)
    #self.assertEqual(type(response), [])
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(len(response.data), 1)

    
