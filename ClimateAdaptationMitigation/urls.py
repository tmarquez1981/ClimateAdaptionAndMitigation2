from django.conf.urls import url
from django.views.generic import TemplateView

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

]
