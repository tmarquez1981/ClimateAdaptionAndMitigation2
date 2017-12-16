from django.conf.urls import url
from django.views.generic import TemplateView
from ClimateAdaptationMitigation.views import FormView, MapView

urlpatterns = [
    #url(r'^home', TemplateView.as_view(template_name="ClimateAdaptationMitigation/html/home.html")),
    #url(r'^map', TemplateView.as_view(template_name="ClimateAdaptationMitigation/html/map.html")),
    #url(r'^contact', TemplateView.as_view(template_name="ClimateAdaptationMitigation/html/contact.html")),
    #url(r'^about', TemplateView.as_view(template_name="ClimateAdaptationMitigation/html/about.html")),
    #url(r'^scope', TemplateView.as_view(template_name="ClimateAdaptationMitigation/html/scope.html")),
    #url(r'^type', TemplateView.as_view(template_name="ClimateAdaptationMitigation/html/type.html")),

        url(r'^home', TemplateView.as_view(template_name="home.html")),
        url(r'^map', TemplateView.as_view(template_name="map.html")),
        url(r'^contact', TemplateView.as_view(template_name="contact.html")),
        url(r'^about', TemplateView.as_view(template_name="about.html")),
        url(r'^scope', TemplateView.as_view(template_name="scope.html")),
        url(r'^type', TemplateView.as_view(template_name="type.html")),
        #url(r'^organizationmap', TemplateView.as_view(template_name="organizationmap.html")),
        #url(r'^form', TemplateView.as_view(template_name="form.html")),
        url(r'^form/$', FormView.as_view(), name='post'),
        url(r'^organizationmap/$', MapView.as_view(), name='post'),
        url(r'^page/(?P<id>\d+)/$', FormView.as_view(), name='post_detail'),
        url(r'^page/(?P<id>\d+)/$', FormView.as_view(), name='post_update'),
        url(r'^page/(?P<id>\d+)/$', FormView.as_view(), name='post_delete'),

        #to update an html page depending on an id pulled from the database:
        #url(r'^page/(?P<id>\d+)/$', name='something')
        #add extram parameter in view function:
        #def post_detail(request, id=None):
]
