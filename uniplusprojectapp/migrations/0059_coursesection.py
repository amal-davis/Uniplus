# Generated by Django 5.0.3 on 2024-09-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0058_degreesection'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='course_videos/')),
            ],
        ),
    ]
