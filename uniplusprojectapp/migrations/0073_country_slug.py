# Generated by Django 5.0.3 on 2024-09-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0072_pg_1st_box_pg_2nd_box_pg_3rd_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.SlugField(default='temp-slug', unique=True),
        ),
    ]
