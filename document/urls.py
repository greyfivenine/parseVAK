from django.urls import path

from .views import *

urlpatterns = [
    path('', get_index_page, name='get_index_page'),
    path('faq/', get_faq_page, name='get_faq_page'),
    path('feedback/', get_feedback_page, name='get_feedback_page'),
    path('documents/', DocumentList.as_view(), name='get_documents_page'),
    path('documents/<str:slug>', get_document_content, name='get_document_content'),
]
