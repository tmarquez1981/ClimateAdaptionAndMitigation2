from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^home', TemplateView.as_view(template_name="ClimateAdaptationMitigation/html/home.html")),
    url(r'^map', TemplateView.as_view(template_name="ClimateAdaptationMitigation/html/map.html")),
    url(r'^contact', TemplateView.as_view(template_name="ClimateAdaptationMitigation/html/contact.html")),
    url(r'^about', TemplateView.as_view(template_name="ClimateAdaptationMitigation/html/about.html")),


]
