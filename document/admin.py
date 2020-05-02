from django.contrib import admin

from .models import Person, CertificateNumber, University, Preamble, Council, Document, DocumentRow

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    class Meta:
        model = Person

    list_display = ['full_name', 'nationality']
    search_fields = ['full_name']

class CertificateNumberAdmin(admin.ModelAdmin):
    class Meta:
        model = CertificateNumber

    list_display = [field.name for field in CertificateNumber._meta.fields]
    search_fields = ['person__full_name', 'certificate_number']

class UniversityAdmin(admin.ModelAdmin):
    class Meta:
        model = University

    list_display = [field.name for field in University._meta.fields]
    search_fields = ['university_name']

class PreambleAdmin(admin.ModelAdmin):
    class Meta:
        model = Preamble

    list_display = [field.name for field in Preamble._meta.fields]
    search_fields = ['preamble_short', 'preamble']

class CouncilAdmin(admin.ModelAdmin):
    class Meta:
        model = Council

    list_display = [field.name for field in Council._meta.fields]

class DocumentAdmin(admin.ModelAdmin):
    class Meta:
        model = Document

    list_display = [field.name for field in Document._meta.fields]
    list_filter = ['document_type', 'document_date']
    search_fields = ['document_name', 'document_number']

class DocumentRowAdmin(admin.ModelAdmin):
    class Meta:
        model = DocumentRow

    list_display = ['document', 'certificate_number', 'science', 'speciality', 'rank', 'degree']
    list_filter = ['document']
    search_fields = ['certificate_number__certificate_number', 'speciality__speciality_name', 'science__science_name']

admin.site.register(Person, PersonAdmin)
admin.site.register(CertificateNumber, CertificateNumberAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Preamble, PreambleAdmin)
admin.site.register(Council, CouncilAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentRow, DocumentRowAdmin)
