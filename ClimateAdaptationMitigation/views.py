from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ClimateAdaptationMitigation.forms import FormForm
from .models import Entity

# Create your views here.


class FormView(TemplateView):
    template_name = 'form.html'

    def get(self, request):
        form = FormForm()
        entities = Entity.objects.all() #returns all the objects in the database

        args = {'form': form, 'entities': entities}
        return render(request, self.template_name, args)

    def post(self, request):
        form = FormForm(request.POST)
        if form.is_valid():
            post = form.save(commit=Fales)#do something with the post object
            #stuff to do with post object here...
            post.save()
            # for security
            text = form.clean_data('post') #field name
            form = HomeForm()
            return redirect('form:form') #returns a blank page

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
