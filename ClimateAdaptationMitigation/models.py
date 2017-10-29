#The model class
#models for the databases
#each class is a table
#run "python manage.py makemigrations" on cmd line when making changes to
#model class
#then, run "python manage.py migrate" to finish migration

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible #for python 2 users

##models.Models allow to save data from class to database
class Entity(models.Model):
    abbreviation = models.CharField(max_length=10) ##VARCHAR(10)
    label = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    scopeCleaned = models.CharField(max_length=20)
    institutionType = models.CharField(max_length=20)
    issueFocus = models.CharField(max_length=20)
    latitidue = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    sources = models.CharField(max_length=40)
    description = models.TextField(blank=True)  #field for adding description
                                                #of Entity
                                                #can be null
    def _str_(self):
        return "Entity: {}".format(self.abbreviation)

@python_2_unicode_compatible
class Nodes(models.Model):
    source = models.CharField(max_length=10)
    target = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
    ##id = models.IntegerField()
    weight = models.IntegerField()
    affiltype = models.CharField(max_length=20)
    regultype = models.CharField(max_length=20)


    def _str_(self):
        return "Nodes: {}".format(self.abbreviation)
