#sets up admin
#admin credentials
#   username: admin
#   password: Emergency2017
#   emailaddress: tmarquez@alaska.edu

from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from django.contrib import admin

# Register your models here.
from .models import Entity
from .models import Edges


from .resources import EntityResource
from .resources import EdgeResource

class EntityAdmin(ImportExportModelAdmin, ImportExportMixin):
    resource_class = EntityResource

class EdgesAdmin(ImportExportModelAdmin, ImportExportMixin):
    resource_class = EdgeResource

admin.site.register(Entity, EntityAdmin)
admin.site.register(Edges, EdgesAdmin)
