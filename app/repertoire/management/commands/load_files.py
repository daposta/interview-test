from django.core.management.base import BaseCommand, CommandError
import os
from pathlib import Path
import csv
from repertoire.models import File, Work

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
      path = (Path(Path.cwd()))
      
      ROOT_DIR = path.parent
      files_dir = os.path.join(ROOT_DIR, "files")
      
      for file in os.listdir(files_dir):
        file_obj = File.objects.create(filename = file)
        
        full_file_path = files_dir + '/' + file
        myfile = open(full_file_path)
        csvreader = csv.reader(myfile)
        header = next(csvreader)
        
        for row in csvreader:
          
          contributor_list = row[1].split('|')
          
          Work.objects.create(title = row[0], contributors= contributor_list, iswc = row[2], 
            source = row[3], proprietary_id = row[4], file_id = file_obj  )
        myfile.close()
