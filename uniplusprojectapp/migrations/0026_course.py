# Generated by Django 5.0.4 on 2024-07-01 04:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0025_university_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('deadline', models.DateField()),
                ('degree', models.CharField(max_length=100)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='uniplusprojectapp.university')),
            ],
        ),
    ]
