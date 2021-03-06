from __future__ import division
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.template.response import TemplateResponse
import csv
from os.path import abspath, dirname
import os
from django.template import RequestContext
from django.utils.encoding import smart_str
#from django.urls import reverse
#from py4j.java_gateway import JavaGateway
import subprocess
#from django.db.models.loading import get_model

from ClimateAdaptationMitigation.forms import FormForm
from ClimateAdaptationMitigation.edgeform import EdgeForm
from .models import Entity, Edges
import random
from django.http import HttpResponse
from django.db.models import Q


# Create views here.

# def search(request):
#     template = 'test.html'
#     data = Entity.objects.all();
#
#     query = request.GET.get('q')
#
#     results = Entity.objects.filter(Q(Abr__icontains=query))
#
#     args = {'results': results}
#
#     return render(request, self.template_name, args)


class legendView(TemplateView):
    template_name = 'test.html'

    def get(self, request):

        # Get all attributes of the "Entities" in the database
        data = Entity.objects.all()
        # Get the count of each filtered object by scope
        totalEntities = Entity.objects.count()
        totalInternational = Entity.objects.filter(ScopeCleaned__startswith='International').count()
        totalLocal = Entity.objects.filter(ScopeCleaned__startswith='Local').count()
        totalRegional = Entity.objects.filter(ScopeCleaned__startswith='Regional').count()
        totalNational = Entity.objects.filter(ScopeCleaned__startswith='National').count()
        totalState = Entity.objects.filter(ScopeCleaned__startswith='State').count()
        totalNull1 = Entity.objects.filter(ScopeCleaned__startswith='Null').count()
        # Get the count of each filtered object by type
        totalGovernment = Entity.objects.filter(InstitutionalType__startswith='Government').count()
        totalNGO = Entity.objects.filter(InstitutionalType__startswith='NGO').count()
        totalTribal = Entity.objects.filter(InstitutionalType__startswith='Tribal').count()
        totalForProfit = Entity.objects.filter(InstitutionalType__startswith='ForProfit').count()
        totalAcademic = Entity.objects.filter(InstitutionalType__startswith='Academic').count()
        totalNull2 = Entity.objects.filter(InstitutionalType__startswith='Null').count()

        # Get percentages of each Organization scope
        internationalPercent = str( round(((totalInternational / totalEntities) * 100),2) ) + '%'
        localPercent = str( round(((totalLocal / totalEntities) * 100),2) ) + '%'
        regionalPercent = str( round(((totalRegional / totalEntities) * 100),2) ) + '%'
        nationalPercent = str( round(((totalNational / totalEntities) * 100),2) ) + '%'
        statePercent = str( round(((totalState / totalEntities) * 100),2) ) + '%'
        nullPercent1 = str( round(((totalNull1 / totalEntities) * 100),2) ) + '%'

        # Get percentages of each Institution Type
        governmentPercentage = str( round(((totalGovernment / totalEntities) * 100),2) ) + '%'
        NGOPercentage = str( round(((totalNGO / totalEntities) * 100),2) ) + '%'
        tribalPercentage = str( round(((totalTribal / totalEntities) * 100),2) ) + '%'
        forProfitPercentage = str( round(((totalForProfit / totalEntities) * 100),2) ) + '%'
        academicPercentage = str( round(((totalAcademic / totalEntities) * 100),2) ) + '%'
        nullPercent2 = str( round(((totalNull2 / totalEntities) * 100),2) ) + '%'


        context = {
            'data': data,
            'internationalPercent': internationalPercent,
            'localPercent': localPercent,
            'regionalPercent': regionalPercent,
            'nationalPercent': nationalPercent,
            'statePercent': statePercent,
            'nullPercent1': nullPercent1,
            
            'governmentPercentage': governmentPercentage,
            'NGOPercentage': NGOPercentage,
            'tribalPercentage': tribalPercentage,
            'forProfitPercentage': forProfitPercentage,
            'academicPercentage': academicPercentage,
            'nullPercent2': nullPercent2
        }
        return render(request, self.template_name, context)


#view for the organization form
class FormView(TemplateView):
    form_template_name = 'form.html'
    delete_template_name = 'delete.html'
    detail_template_name = 'detail.html'
    update_template_name = 'update.html'
    home_template_name = 'home.html'
    edgeform_template_name = '../edgeform.html'

    def get(self, request):
        form = FormForm()
        #instance = get_object_or_404(Edges, id=2)
        entities = Entity.objects.all() #returns all the objects in the database

        #get current working directory
        currenDir = abspath(dirname(__file__))
        #testing to see if gephi jar file call works...
        # subprocess.call(['java', '-jar', currenDir + '/gephi-0.9.2.jar'])

        args = {'form': form, 'entities': entities}
        return render(request, self.form_template_name, args)

    def post(self, request):
        form = FormForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)#do something with the post object
                #stuff to do with post object here...
                post.save()
                messages.success(request, "Successfully Created")

                return HttpResponseRedirect(self.edgeform_template_name)

        else:
            messages.error(request, "Not Successfully Created")
            args = {'form': form, 'entities': entities}
            return render(request, self.form_template_name, args)

    def post_detail(self, request):
        #use when finished implmenting roles
        #if request.user.is_authenticated():
        queryset = Post.objects.all()
        context = {
        "object_list": queryset

        }
        return render(request, "test.html", context)

#view for the Google maps api
class MapView(TemplateView):
    template_name = 'organizationmap.html'

    def get(self, request):
        form = FormForm()
        queryset = Entity.objects.all() #returns all the objects in the database
        queryset = serializers.serialize('json', queryset)

        args = {'form': form, 'queryset': queryset}
        return render(request, self.template_name, args)

    #to update/edit
    def post_update(request, id=None):
        instance = get_object_or_404(Entity, id=id)
        form = FormForm(request.POST or None, instance=instance)
        if form.is_valid():
            post = form.save(commit=False)#do something with the post object
            #stuff to do with post object here...
            post.save()
            messages.success(request, "Successfully Updated")
            # for security
            #text = form.clean_data('post') #field name
            form = FormForm()
        else:
            messages.error(request, "Not Successfully Updated")

        def post_delete(request, id=None):
            instance = get_object_or_404(Entity, id=id)
            instance.delete()
            messages.success(request, "Successfully Deleted")

            return redirect(self.home_template_name)

        def list(request):
            queryset = Entity.objects.all()

            queryset = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            queryset = unescape({{queryset | safe | escapejs}});
            queryset = JSON.parse(queryset);

            return TemplateResponse(request, '/templates/organizationmap.html', {})
            #return TemplateResponse(request, '/static/templates/organizationmap.html', {})

#view for the Google maps api / using for test.html
class MapView2(TemplateView):
    template_name = 'test.html'

    def get(self, request):
        form = FormForm()
        queryset = Entity.objects.all() #returns all the objects in the database
        queryset = serializers.serialize('json', queryset)

        args = {'form': form, 'queryset': queryset}
        return render(request, self.template_name, args)

    #to update/edit
    def post_update(request, id=None):
        instance = get_object_or_404(Entity, id=id)
        form = FormForm(request.POST or None, instance=instance)
        if form.is_valid():
            post = form.save(commit=False)#do something with the post object
            #stuff to do with post object here...
            post.save()
            messages.success(request, "Successfully Updated")
            # for security
            #text = form.clean_data('post') #field name
            form = FormForm()
        else:
            messages.error(request, "Not Successfully Updated")

        def post_delete(request, id=None):
            instance = get_object_or_404(Entity, id=id)
            instance.delete()
            messages.success(request, "Successfully Deleted")

            return redirect(self.home_template_name)

        def list(request):
            queryset = Entity.objects.all()

            queryset = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            queryset = unescape({{queryset | safe | escapejs}});
            queryset = JSON.parse(queryset);

            return TemplateResponse(request, '/static/templates/test.html', {})


#view for the edge form
class EdgeView(TemplateView):
    template_name = 'edgeform.html'
    home_template_name = 'home.html'

    def get(self, request):
        form = EdgeForm()
        queryset = Edges.objects.all() #returns all the objects in the database
        print("this")

        args = {'form': form, 'queryset': queryset}
        return render(request, self.template_name, args)

    def post(self, request):
        form = EdgeForm(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                print("this")
                post = form.save(commit=False)#do something with the post object
                #stuff to do with post object here...
                post.types = 'undirected'
                post.save()
                messages.success(request, "Successfully Created")

                #write edges model to edges.gdf after post is successful
                edges = Edges.objects.all()
                entities = Entity.objects.all()
                #edges = Edges._meta.fields
                #get directory of manage.py and append location of gdf file
                currenDir = os.getcwd()
                path = currenDir + '/static/files/edges.gdf'
                self.writeToGDF(entities, edges, path)

                #run gephi
                self.runGephi()

                #return to home page
                return HttpResponseRedirect(self.home_template_name)

        else:
            messages.error(request, "Not Successfully Created")
            #args = {'form': form, 'text': text}
            args = {'form': form, 'queryset': queryset}
            return render(request, self.form_template_name, args)

    # method model to the gdf file
    # parameters are the queryset and the file name
    # TODO: currently very inificient since it rewrites the entire queryset
    # from the database. Seemed simpler to implement at the moment
    # a GDF file is similar to a CSV, so thoeritically this should work
    # references site: http://palewi.re/posts/2009/03/03/django-recipe-dump-your-queryset-out-as-a-csv-file/
    def writeToGDF(self, qsEntity, qsEdges, file_path):
        #model = qs.model
        writer = csv.writer(open(file_path, 'w'))

        #writes the headers for nodes to file
        writer.writerow([
            smart_str(u"nodedef>name VARCHAR"),
            smart_str(u"label VARCHAR"),
            smart_str(u"location VARCHAR"),
            smart_str(u"scope VARCHAR"),
            smart_str(u"type VARCHAR"),
            smart_str(u"issue VARCHAR"),
            smart_str(u"lat DOUBLE"),
            smart_str(u"lng DOUBLE"),
        ])

        for obj in qsEntity:
            writer.writerow([
            smart_str(obj.Abr),
            smart_str(obj.Label),
            smart_str(obj.Location),
            smart_str(obj.ScopeCleaned),
            smart_str(obj.InstitutionalType),
            smart_str(obj.IssueFocus),
            smart_str(obj.Lat),
            smart_str(obj.Lng),
            smart_str(obj.source),
            smart_str(obj.description),
            ])

        #write headers for edges
        writer.writerow([
            smart_str(u"edgedef>node1 VARCHAR"),
            smart_str(u"node2 VARCHAR"),
            smart_str(u"type BOOLEAN"),
            smart_str(u"AffilType VARCHAR"),
            smart_str(u"RegulType VARCHAR"),
        ])

        #loop through all the edges and write to file
        for obj in qsEdges:
            writer.writerow([
            smart_str(obj.source),
            smart_str(obj.target),
            smart_str(obj.types),
            smart_str(obj.affiltype),
            smart_str(obj.regultype),
        ])

    #TODO:function will successfully run a jar file, but pathing issues with
    # the file names cause an null pointer
    #function to run gephi after post to edge forms
    #refernced from https://stackoverflow.com/questions/7372592/python-how-can-i-execute-a-jar-file-through-a-python-script/7372651
    def runGephi(self):
        currenDir = abspath(dirname(__file__))
        subprocess.call(['java', '-jar', currenDir + '/gephi-0.9.2.jar'])

#TODO:view for the contact form



"""
class ContactForm(TemplateView):

    def get(self, request):
        form = ContactForm()
        queryset = Contact.objects.all() #returns all the objects in the database
        print("this")

        args = {'form': form, 'queryset': queryset}
        return render(request, self.template_name, args)

    def post(self, request):
        form = ContactForm(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                print("this")
                post = form.save(commit=False)#do something with the post object
                #stuff to do with post object here...
                post.types = 'undirected'
                post.save()
                messages.success(request, "Successfully Created")

                #write edges model to edges.gdf after post is successful
                edges = Edges.objects.all()
                #edges = Edges._meta.fields
                path = '/home/tom/Climate/bin/Climate/static/files/edges.gdf'
                self.writeToGDF(edges, path)

                #run gephi
                self.runGephi()

                #return to home page
                return HttpResponseRedirect(self.home_template_name)

        else:
            messages.error(request, "Not Successfully Created")
            #args = {'form': form, 'text': text}
            args = {'form': form, 'queryset': queryset}
            return render(request, self.form_template_name, args)
"""
