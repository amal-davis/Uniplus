# Generated by Django 5.0.3 on 2024-07-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0033_travelhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelhistory',
            name='visa_countries',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='travelhistory',
            name='visa_rejections',
            field=models.BooleanField(default=False),
        ),
    ]