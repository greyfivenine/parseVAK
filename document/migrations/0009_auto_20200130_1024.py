# Generated by Django 3.0.1 on 2020-01-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0008_auto_20200129_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentrow',
            name='certificate_number',
        ),
        migrations.RemoveField(
            model_name='documentrow',
            name='registration_date',
        ),
        migrations.AddField(
            model_name='person',
            name='certificate_number',
            field=models.CharField(default='', max_length=30, verbose_name='Номер аттестационного дела'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='registration_date',
            field=models.DateTimeField(default='1970-01-01 00:00', verbose_name='Дата регистрации'),
            preserve_default=False,
        ),
    ]