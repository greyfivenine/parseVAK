# Generated by Django 3.0.3 on 2020-04-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0017_auto_20200224_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя отправителя')),
                ('email', models.CharField(max_length=70, verbose_name='Email')),
                ('theme', models.CharField(max_length=100, verbose_name='тема сообщения')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
            ],
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-document_date']},
        ),
    ]
