# Generated by Django 5.0.3 on 2024-09-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0060_delete_ugprograminformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('button_text', models.CharField(blank=True, max_length=255, null=True)),
                ('button_link', models.URLField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='contact_images/')),
            ],
        ),
    ]