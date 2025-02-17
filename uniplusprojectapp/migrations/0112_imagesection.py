# Generated by Django 5.0.3 on 2024-11-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0111_predeparturesection'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('position', models.CharField(choices=[('large', 'Large Item'), ('small', 'Small Item'), ('full', 'Full-Width Item')], max_length=10)),
            ],
        ),
    ]
