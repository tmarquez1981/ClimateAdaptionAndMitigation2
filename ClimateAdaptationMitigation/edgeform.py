#python file for the edge form

from django import forms
from .models import Edges

#for the user form
class EdgeForm(forms.ModelForm):

    AFFILTYPES = (
        ('ScienceData', 'ScienceData'), ('Multiple', 'Multiple'), ('Funder', 'Funder'),
        ('GovernanceLegal', 'GovernanceLegal'), ('Other', 'Other'), ('none', 'none')
        )

    REGTYPES = (
        ('Informal', 'Informal'), ('FormalMOU', 'FormalMOU'), ('Funder', 'Funder'),
        ('none', 'none')
        )

    source = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'name of your organization'
        }))

    target = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'name of the organization you are connected to'
        }))

    types = forms.CharField(required=False)

    affiltype = forms.CharField(widget=forms.Select(choices=AFFILTYPES))

    regultype = forms.CharField(widget=forms.Select(choices=REGTYPES))

    class Meta:
        model = Edges
        fields = ('source', 'target', 'types', 'affiltype',
                'regultype',)
