from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.sessions.models import Session
from django.utils import timezone

from .models import Document, DocumentRow, Feedback
from .forms import SearchForm, FastSearchForm, FeedbackForm
# Create your views here.

def get_index_page(request):
    flag = True
    active_header = 'index'
    context = {
        'flag':flag,
        'active_header':active_header
    }
    if 'person_name' in request.GET.keys():
        context['flag'] = False
        form_data = request.GET
        bound_form = FastSearchForm(form_data)
        if bound_form.is_valid():
            search_result = DocumentRow.objects.filter(certificate_number__person__full_name__contains=bound_form.cleaned_data['person_name'])
            context['search_result'] = search_result
            context['person_name'] = bound_form.cleaned_data['person_name']
            return render(request, 'document/index.html', context = context)
        else:
            raise Http404('Page not found')
    else:
        return render(request, 'document/index.html', context = context)

def get_faq_page(request):
    active_header = 'faq'
    return render(request, 'document/faq.html', context = {'active_header':active_header})

def get_document_content(request, slug):
    active_header = 'search'
    doc = Document.objects.get(document_slug__iexact=slug)

    doc_type_id = doc.document_type_id
    if doc.document_type_id == 3:
        doc_rows = doc.doc_rows.order_by('degree', 'science', 'certificate_number__person__full_name')
    elif doc.document_type_id == 2:
        doc_rows = doc.doc_rows.order_by('rank', 'certificate_number__person__full_name')
    return render(request, 'document/doc_content.html', context = {'doc_rows':doc_rows, 'doc':doc, 'active_header':active_header})

class FeedbackView(View):
    def get(self, request):
        active_header = 'feedback'
        return render(request, 'document/feedback.html', context = {'active_header':active_header})
    def post(self, request):
        active_header = 'feedback'
        if 'pause' not in request.session:
            form_data = request.POST
            bound_form = FeedbackForm(form_data)
            if bound_form.is_valid():
                cleaned_data = bound_form.cleaned_data
                fb = Feedback(**cleaned_data)
                request.session.set_expiry(900)
                request.session['pause'] = True
                fb.save()
                return render(request, 'document/feedback.html', context = {'active_header':active_header, 'errors':False, 'flag':True})
            return render(request, 'document/feedback.html', context = {'active_header':active_header, 'errors':bound_form.errors, 'flag':True})
        else:
            session = Session.objects.get(session_key=request.session.session_key)

            remaining_seconds = session.expire_date - timezone.now()
            remaining_seconds = remaining_seconds.total_seconds()

            errors = {'err': 'Ошибка. Попробуйте отправить ваш отзыв через {0} минут {1} секунд'.format(int(remaining_seconds // 60), int(remaining_seconds % 60))}
            return render(request, 'document/feedback.html', context = {'active_header':active_header, 'errors':errors, 'flag':True})

class DocumentListView(View):
    def get(self, request):
        active_header = 'search'
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
                'active_header':active_header,
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
