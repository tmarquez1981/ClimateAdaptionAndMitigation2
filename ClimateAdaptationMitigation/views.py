from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.template.response import TemplateResponse
import csv
import os.path
import os
from django.utils.encoding import smart_str
from django.urls import reverse
#from py4j.java_gateway import JavaGateway
import subprocess
#from django.db.models.loading import get_model

from ClimateAdaptationMitigation.forms import FormForm
from ClimateAdaptationMitigation.edgeform import EdgeForm
from .models import Entity, Edges

# Create views here.

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

        #cwd = os.getcwd()
        subprocess.call(['java', '-jar', '/home/tom/Climate/bin/Climate/ClimateAdaptationMitigation/mavenproject1-1.0-SNAPSHOT.jar'])

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
            #args = {'form': form, 'text': text}
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

            return TemplateResponse(request, '/static/templates/organizationmap.html', {})

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

    # method model to the gdf file
    # parameters are the queryset and the file name
    # TODO: currently very inificient since it rewrites the entire queryset
    # from the database. Seemed simpler to implement at the moment
    # a GDF file is similar to a CSV, so thoeritically this should work
    # references site: http://palewi.re/posts/2009/03/03/django-recipe-dump-your-queryset-out-as-a-csv-file/
    def writeToGDF(self, qs, file_path):
        #model = qs.model
        writer = csv.writer(open(file_path, 'w'))

        #writes the headers to file
        writer.writerow([
            smart_str(u"edgedef>node1 VARCHAR"),
            smart_str(u"node2 VARCHAR"),
            smart_str(u"type BOOLEAN"),
            smart_str(u"AffilType VARCHAR"),
            smart_str(u"RegulType VARCHAR"),
        ])

        #loop through all the edges and write to file
        for obj in qs:
            writer.writerow([
            smart_str(obj.source),
            smart_str(obj.target),
            smart_str(obj.types),
            smart_str(obj.affiltype),
            smart_str(obj.regultype),
        ])

    #function to run gephi after post to edge forms
    #refernced from https://stackoverflow.com/questions/7372592/python-how-can-i-execute-a-jar-file-through-a-python-script/7372651
    def runGephi(self):
        subprocess.call(['java', '-jar', '/home/tom/Climate/bin/Climate/ClimateAdaptationMitigation/mavenproject1-1.0-SNAPSHOT.jar'])

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
