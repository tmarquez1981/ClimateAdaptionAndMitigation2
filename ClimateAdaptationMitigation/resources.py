# resources.py
# for import/export of csv files to/from databases

from import_export import resources

from .models import Nodes

class NodesResource(resources.ModelsResource):
    class Meta:
        model = Nodes
