#The model class
#models for the databases
#each class is a table
#run "python manage.py makemigrations" on cmd line when making changes to
#model class
#then, run "python manage.py migrate" to finish migration

#For database shell, run "python manage.py dbshell" from command line

#To look at objects in database, close server and run "shell"
#type the following in shell prompt:
#from ClimateAdaptationMitigation.models import post
#Post.objecst.all()

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

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
    date = models.DateTimeField(auto_now=True)#timestamp of post

    def __str__(self):
        return "Entity: {}".format(self.Abr)

    def get_absolute_url(self):
        return "/entities/%s/" %(self.id)
        #return reverse("NameOfUrl", kwargs={"id": self.id})


@python_2_unicode_compatible
class Edges(models.Model):
    source = models.CharField(max_length=10)
    target = models.CharField(max_length=10)
    types = models.CharField(max_length=15)
    ##id = models.IntegerField()
    affiltype = models.CharField(max_length=20)
    regultype = models.CharField(max_length=20)

    ##displays the objects in a "Source: <source name> Target: <target name> " format
    def __str__(self):
        return "Source: {0} Target: {1}".format(self.source, self.target)

    def get_absolute_url(self):
        return "/edges/%s/" %(self.id)
