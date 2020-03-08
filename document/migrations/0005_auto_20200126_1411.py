# Generated by Django 3.0.1 on 2020-01-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_auto_20200118_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='document',
            name='document_slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='full_name',
            field=models.CharField(default='', max_length=110, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='nationality',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='Гражданство'),
        ),
        migrations.AlterField(
            model_name='documentrow',
            name='decision_num',
            field=models.CharField(blank=True, default='', max_length=4, null=True, verbose_name='Номер решения'),
        ),
    ]