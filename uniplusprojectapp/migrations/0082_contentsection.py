# Generated by Django 5.0.3 on 2024-10-13 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0081_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
