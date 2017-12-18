# resources.py
# for import/export of csv files to/from databases

from import_export import resources
from import_export import fields

from .models import Entity
from .models import Edges

class EntityResource(resources.ModelResource):
    class Meta:
        model = Entity
        #fields = ('abbreviation', 'label', 'location', 'scopeCleaned',
        #        'institutionType', 'issueFocus', 'latitidue', 'longitude',
        #        'sources', 'description',)

        # allows import of csv file without id explicitly in file
        import_id_fields = ('Abr', 'Label', 'Location', 'ScopeCleaned',
               'InstitutionalType', 'IssueFocus', 'Lat', 'Lng',
               'source',)

class EdgeResource(resources.ModelResource):
    class Meta:
        model = Edges
        import_id_fields = ('source', 'target', 'types', 'affiltype', 'regultype',)
