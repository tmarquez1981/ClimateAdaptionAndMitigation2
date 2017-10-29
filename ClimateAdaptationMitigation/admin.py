#sets up admin
#admin credentials
#   username: admin
#   password: Emergency2017
#   emailaddress: tmarquez@alaska.edu

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin


# Register your models here.
from .models import Entity
from .models import Edges

admin.site.register(Entity)
admin.site.register(Edges)

class NodesAdmin(ImportExportModelAdmin):
    pass
