# Generated by Django 5.0.3 on 2024-07-15 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0047_rename_is_read_notification_read_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='course_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='university_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]