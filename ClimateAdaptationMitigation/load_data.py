##python script to load csv file

import django
import os
#import csv.sys.os
import csv

from .models import Entity

project_dir = "/home/tom/Climate/bin/Climate/Climate"

os.environ['DJANGO_SETTINGS_MODULE'] = 'Climate.settings'

django.setup()


with open('/SOAClimateMappingProject_Entities.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'Abr': ##skip the header row
                print(row)
                #_, created = Entity.objects.get_or_create(
                #abbreviation=row[0],
                #label=row[1],
                #location=row[2],
                #scopeCleaned=row[3],
                #institutionType=row[4],
                #issueFocus=row[5],
                #latitidue=row[6],
                #longitude=row[7],
                #sources=row[8],
                #)
