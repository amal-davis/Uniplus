# Generated by Django 5.0.3 on 2024-10-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0083_remove_contentsection_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catrer_counselling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
