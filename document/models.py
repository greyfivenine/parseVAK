from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя отправителя")
    email = models.CharField(max_length=70, verbose_name="Email")
    theme = models.CharField(max_length=100, verbose_name="Тема сообщения")
    text = models.TextField(verbose_name="Текст сообщения")

    def __str__(self):
        return 'Тема: {0}, От: {1}'.format(self.theme, self.name)

class Person(models.Model):
    full_name = models.CharField(max_length=110, db_index=True, verbose_name="ФИО")
    nationality = models.CharField(max_length=40, blank=True, null=True, default='', verbose_name="Гражданство")

    def __str__(self):
        return '{}'.format(self.full_name)

class CertificateNumber(models.Model):
    certificate_number = models.CharField(max_length=30, verbose_name="Номер аттестационного дела")
    registration_date = models.DateTimeField(verbose_name="Дата регистрации")
    person = models.ForeignKey('Person', on_delete=models.CASCADE, db_index=True, verbose_name="УИД человека")

    def __str__(self):
        return '{}'.format(self.certificate_number)

class Science(models.Model):
    science_name = models.CharField(max_length=50, verbose_name="Наименование науки")

    def __str__(self):
        return self.science_name

class Degree(models.Model):
    degree_name = models.CharField(max_length=8, verbose_name="Наименование степени")

    def __str__(self):
        return self.degree_name

class Rank(models.Model):
    rank_name = models.CharField(max_length=9, verbose_name="Наименование звания")

    def __str__(self):
        return self.rank_name

class Speciality(models.Model):
    speciality_name = models.CharField(max_length=150, db_index=True, verbose_name="Наименование специальности")
    speciality_code = models.CharField(max_length=8, verbose_name="Код специальности")

    def __str__(self):
        return self.speciality_name

class University(models.Model):
    university_name = models.CharField(max_length=250, db_index=True, verbose_name="Наименование университета")
    preamble = models.ForeignKey('Preamble', on_delete=models.CASCADE, verbose_name="УИД преамбулы")

    def __str__(self):
        return '{0} {1}'.format(self.preamble.preamble_short, self.university_name)

class Preamble(models.Model):
    preamble_short = models.CharField(max_length=10, db_index=True, verbose_name="Преамбула кор.")
    preamble = models.CharField(max_length=150, verbose_name="Преамбула")

class Council(models.Model):
    council_code = models.CharField(max_length=20, verbose_name="Код совета")
    universities = models.ManyToManyField('University', related_name='universities', verbose_name="Состав совета")
    specialities = models.ManyToManyField('Speciality', related_name='councils', verbose_name="Сфера совета")

    def __str__(self):
        return '; '.join([value.__str__() for value in self.universities.all()])

class DocumentType(models.Model):
    type = models.CharField(max_length=51)

    def __str__(self):
        return self.type

class Document(models.Model):
    document_slug = models.SlugField(max_length=50, unique=True)
    document_create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания документа")
    document_date = models.DateTimeField(verbose_name="Дата публикации документа")
    document_name = models.CharField(max_length=150, db_index=True, verbose_name="Наименование документа")
    document_number = models.CharField(max_length=10, db_index=True, verbose_name="Номер документа")
    document_type = models.ForeignKey('DocumentType', on_delete=models.CASCADE, db_index=True, verbose_name="УИД типа документа")
    document_link = models.CharField(max_length=100, verbose_name="Ссылка на документ")

    def get_absolute_url(self):
        return reverse('get_document_content', kwargs={'slug': self.document_slug})

    def __str__(self):
        return self.document_number

    class Meta:
        ordering = ['-document_date']

class DocumentRow(models.Model):
    document = models.ForeignKey('Document', on_delete=models.CASCADE, verbose_name="УИД документа", related_name="doc_rows")
    certificate_number = models.ForeignKey('CertificateNumber', on_delete=models.CASCADE, verbose_name="УИД аттестационного дела")

    university = models.ForeignKey('University', on_delete=models.CASCADE, verbose_name="УИД ВУЗ", blank=True, null=True)
    speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE, verbose_name="УИД специальности", blank=True, null=True)
    science = models.ForeignKey('Science', on_delete=models.CASCADE, verbose_name="УИД науки", blank=True, null=True)
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE, verbose_name="УИД звания", blank=True, null=True)
    degree = models.ForeignKey('Degree', on_delete=models.CASCADE, verbose_name="УИД степени", blank=True, null=True)
    council = models.ForeignKey('Council', on_delete=models.CASCADE, verbose_name="УИД совета", blank=True, null=True)

    defence_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата защиты")
    decision_num = models.CharField(max_length=30, blank=True, null=True, default='', verbose_name="Номер решения")

    def __str__(self):
        return "Строка документа {0}".format(self.document.document_number)
