# Generated by Django 4.2.4 on 2024-06-28 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0011_aboutteammember'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutteammember',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='aboutteammember',
            name='title',
        ),
    ]
