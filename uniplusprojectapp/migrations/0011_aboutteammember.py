# Generated by Django 4.2.4 on 2024-06-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0010_aboutempowering'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='team_images/')),
            ],
        ),
    ]