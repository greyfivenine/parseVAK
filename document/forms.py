from django import forms
from .models import Document, DocumentType

class SearchForm(forms.Form):
    doc_name = forms.CharField(max_length=100, required=False)
    doc_num = forms.CharField(max_length=10, required=False)
    doc_type = forms.IntegerField(required=False)
    doc_datefrom = forms.DateTimeField(required=False)
    doc_dateto = forms.DateTimeField(required=False)
    page = forms.IntegerField(required=False)
