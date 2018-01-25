#a bound form that is bound to the model
#bound to the entity model

from django import forms
from .models import Entity

#for the user form
class FormForm(forms.ModelForm):

    SCOPE_LIST = (
        ('International', 'International'), ('Local', 'Local'), ('Regional', 'Regional'),
        ('National', 'National'), ('State', 'State'), ('Null', 'Null')
        )

    INSTTYPES = (
        ('Government', 'Government'), ('NGO', 'NGO'), ('Tribal', 'Tribal'),
        ('ForProfit', 'ForProfit'), ('Academic', 'Academic'), ('Null', 'Null')
        )

    ISSUES = (
        ('Broad Climate', 'Broad Climate'), ('Economic', 'Economic'), ('Marine', 'Marine'),
        ('Arctic Sovereignty', 'Arctic Sovereignty'), ('Landscape/Permafrost', 'Landscape/Permafrost'),
        ('Social/Health', 'Social/Health'), ('Transportation/Infrastructure', 'Transportation/Infrastructure'),
        ('Pollution/Carbon Emmissions', 'Pollution/Carbon Emmissions'),
        ('Energy', 'Energy')
        )

    Abr = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Abbreviation for Organization'
        }))
    Label = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name of Organization'
        }))
    Location = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ex: Anchorage, Alaska'
        }))
    ScopeCleaned = forms.CharField(widget=forms.Select(choices=SCOPE_LIST))
    InstitutionalType = forms.CharField(widget=forms.Select(choices=INSTTYPES))
    IssueFocus = forms.CharField(widget=forms.Select(choices=ISSUES))
    Lat = forms.DecimalField()
    Lng = forms.DecimalField()
    source = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'www.place.com'
        }))
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Description'
        }))

    class Meta:
        model = Entity
        #fields = ('Abr', 'Label', 'Location', 'ScopeCleaned',
        #        'InstitutionalType', 'IssueFocus', 'Lat', 'Lng',
        #        'source', 'description,)
        fields = ('Abr', 'Label', 'Location', 'ScopeCleaned',
                'InstitutionalType', 'IssueFocus', 'Lat', 'Lng',
                 'source',)
