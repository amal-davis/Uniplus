# Generated by Django 5.0.3 on 2024-10-13 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0082_contentsection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentsection',
            name='title',
        ),
    ]
