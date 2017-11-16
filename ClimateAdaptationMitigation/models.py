#The model class
#models for the databases
#each class is a table
#run "python manage.py makemigrations" on cmd line when making changes to
#model class
#then, run "python manage.py migrate" to finish migration

#For database shell, run "python manage.py dbshell" from command line

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible #for python 2 users

##models.Models allow to save data from class to database
class Entity(models.Model):
    Abr = models.CharField(max_length=10) ##VARCHAR(10)
    Label = models.CharField(max_length=20)
    Location = models.CharField(max_length=20)
    ScopeCleaned = models.CharField(max_length=20)
    InstitutionalType = models.CharField(max_length=20)
    IssueFocus = models.CharField(max_length=20)
    Lat = models.DecimalField(max_digits=9, decimal_places=6)
    Lng = models.DecimalField(max_digits=9, decimal_places=6)
    source = models.CharField(max_length=40)
    description = models.TextField(blank=True)  #field for adding description
                                                #of Entity
                                                #can be null
    def __str__(self):
        return "Entity: {}".format(self.Abr)


@python_2_unicode_compatible
class Edges(models.Model):
    source = models.CharField(max_length=10)
    target = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
    ##id = models.IntegerField()
    weight = models.IntegerField()
    affiltype = models.CharField(max_length=20)
    regultype = models.CharField(max_length=20)

    ##displays the objects in a "Source: <source name> Target: <target name> " format
    def __str__(self):
        return "Source: {0} Target: {1}".format(self.source, self.target)
