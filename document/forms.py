from django import forms
from .models import Document, DocumentType

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, error_messages={'required': 'Пожалуйста, введите ваше имя.', 'max_length': 'Максимальная длина поля "Ваше имя" - 30 символов.'})
    email = forms.EmailField(max_length=70, required=True, error_messages={'required': 'Пожалуйста, введите ваш email.', 'invalid': 'Введенный вами email неккоретен.'})
    theme = forms.CharField(max_length=100, required=True, error_messages={'required': 'Пожалуйста, введите тему.', 'max_length': 'Максимальная длина поля "Тема письма" - 100 символов.'})
    text = forms.CharField(widget=forms.Textarea, required=True, error_messages={'required': 'Пожалуйста, введите текст сообщения.'})

class SearchForm(forms.Form):
    doc_name = forms.CharField(max_length=100, required=False)
    doc_num = forms.CharField(max_length=10, required=False)
    doc_type = forms.IntegerField(required=False)
    doc_datefrom = forms.DateTimeField(required=False)
    doc_dateto = forms.DateTimeField(required=False)
    page = forms.IntegerField(required=False)

class FastSearchForm(forms.Form):
    person_name = forms.CharField(max_length=100, required=True)
