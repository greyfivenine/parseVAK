from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Document, DocumentRow
from .forms import SearchForm, FastSearchForm

# Create your views here.

def get_index_page(request):
    flag = True
    context = {
        "flag":flag,
    }
    if "person_name" in request.GET.keys():
        context['flag'] = False
        form_data = request.GET
        bound_form = FastSearchForm(form_data)
        if bound_form.is_valid():
            search_result = DocumentRow.objects.filter(certificate_number__person__full_name__contains=bound_form.cleaned_data['person_name'])
            context['search_result'] = search_result
            context['person_name'] = bound_form.cleaned_data['person_name']
            return render(request, 'document/index.html', context = context)
        else:
            raise Http404("Page not found")
    else:
        return render(request, 'document/index.html', context = context)

def get_faq_page(request):
    return render(request, 'document/faq.html')

def get_feedback_page(request):
    return render(request, 'document/feedback.html')

def get_document_content(request, slug):
    doc = Document.objects.get(document_slug__iexact=slug)
    return render(request, 'document/doc_content.html', context = {'doc':doc})

class DocumentList(View):
    def get(self, request):
        form_data = request.GET
        bound_form = SearchForm(form_data)
        if bound_form.is_valid():
            search_result = Document.objects.all()

            if bound_form.cleaned_data['doc_name']:
                search_result = search_result.filter(document_name__contains=bound_form.cleaned_data['doc_name'])
            if bound_form.cleaned_data['doc_num']:
                search_result = search_result.filter(document_number__contains=bound_form.cleaned_data['doc_num'])
            if bound_form.cleaned_data['doc_type']:
                search_result = search_result.filter(document_type__exact=bound_form.cleaned_data['doc_type'])
            if bound_form.cleaned_data['doc_datefrom']:
                search_result = search_result.filter(document_date__gte=bound_form.cleaned_data['doc_datefrom'])
            if bound_form.cleaned_data['doc_dateto']:
                search_result = search_result.filter(document_date__lte=bound_form.cleaned_data['doc_dateto'])

            paginator = Paginator(search_result, 10)
            page_number = bound_form.cleaned_data.get('page', 1)
            page = paginator.get_page(page_number)

            first_page_url = 1
            last_page_url = paginator.num_pages

            context = {
                'page':page,
                'header':'Недавно добавленные',
                'first_page_url':first_page_url,
                'last_page_url':last_page_url,
                'form':bound_form.cleaned_data
            }

            if form_data:
                context['header'] = 'Результат поиска'

            return render(request, 'document/docs_default.html', context = context)
        raise Http404("Page not found")
