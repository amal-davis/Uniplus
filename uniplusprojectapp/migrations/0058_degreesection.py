# Generated by Django 5.0.3 on 2024-09-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0057_delete_degreesection_delete_ugprogramsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='degree_images/')),
            ],
        ),
    ]
