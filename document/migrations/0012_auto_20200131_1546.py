# Generated by Django 3.0.1 on 2020-01-31 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0011_auto_20200130_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='university_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Наименование университета'),
        ),
    ]
