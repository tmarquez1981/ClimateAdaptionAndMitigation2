from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.template.response import TemplateResponse
import csv
#from django.db.models.loading import get_model

from ClimateAdaptationMitigation.forms import FormForm
from .models import Entity, Edges

# Create your views here.


class FormView(TemplateView):
    form_template_name = 'form.html'
    delete_template_name = 'delete.html'
    detail_template_name = 'detail.html'
    update_template_name = 'update.html'
    home_template_name = 'home.html'

    def get(self, request):
        form = FormForm()
        instance = get_object_or_404(Edges, id=2)
        entities = Entity.objects.all() #returns all the objects in the database

        args = {'form': form, 'entities': entities}
        return render(request, self.form_template_name, args)


    def post(self, request):
        form = FormForm(request.POST or None)
        if request.method == "POST":
            print(request.POST)
            if form.is_valid():
                post = form.save(commit=False)#do something with the post object
                #stuff to do with post object here...
                post.save()
                messages.success(request, "Successfully Created")
                # for security
                #text = form.clean_data('post') #field name
                form = FormForm()
                return render(request, self.home_template_name, {})
            #return HttpResponseRedirect(post.get_absolute_url())
            #return redirect('form:form') #returns a blank page
        else:
            messages.error(request, "Not Successfully Created")
            #args = {'form': form, 'text': text}
            args = {'form': form, 'entities': entities}
            return render(request, self.form_template_name, args)

    # method model to the gdf file
    # parameters are the queryset and the file name
    # TODO: currently very inificient since it rewrites the entire queryset
    # from the database. Seemed simpler to implement at the moment
    # a GDF file is similar to a CSV, so thoeritically this should work
    # references site: http://palewi.re/posts/2009/03/03/django-recipe-dump-your-queryset-out-as-a-csv-file/
    def writeToGDF(self, qs, file_path):
        model = qs.model
        writer = csv.writer(open(file_path, 'w'))

        # may need to hardcode headers here since the source code was for
        # writing to a CSV file, not a GDF file
        # header = edgedef>node1 VARCHAR,node2 VARCHAR,type BOOLEAN,AffilType VARCHAR,RegulType VARCHAR
    	#headers = []
    	#for field in model._meta.fields:
    	#	headers.append(field.name)
        header = 'edgedef>node1 VARCHAR,node2 VARCHAR,type BOOLEAN,AffilType VARCHAR,RegulType VARCHAR'
        writer.writerow(headers)

        for obj in qs:
    	    row = []
    	    for field in headers:
    		    val = getattr(obj, field)
    		    if callable(val):
    			    val = val()
    		    if type(val) == unicode:
    			    val = val.encode("utf-8")
    		    row.append(val)
    	    writer.writerow(row)

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
            #queryset = serializers.serialize('json', queryset)
            queryset = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            queryset = unescape({{queryset | safe | escapejs}});
            queryset = JSON.parse(queryset);
            #prices_json = json.dumps(list(prices), cls=DjangoJSONEncoder)
            return TemplateResponse(request, '/static/templates/organizationmap.html', {})
