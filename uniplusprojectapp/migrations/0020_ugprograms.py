# Generated by Django 4.2.4 on 2024-06-29 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0019_ugprograminformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='UgPrograms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
