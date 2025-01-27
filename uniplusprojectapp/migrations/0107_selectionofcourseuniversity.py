# Generated by Django 5.0.3 on 2024-10-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0106_job_remote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selectionofcourseuniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of the degree section', max_length=200)),
                ('description', models.TextField(help_text='Enter the description for the degree section')),
                ('image', models.ImageField(blank=True, null=True, upload_to='degree_images/')),
            ],
        ),
    ]
