# Generated by Django 4.2.14 on 2024-08-22 03:10

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_quill.fields.QuillField(),
        ),
    ]
