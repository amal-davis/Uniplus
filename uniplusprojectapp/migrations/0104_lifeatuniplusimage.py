# Generated by Django 5.0.3 on 2024-10-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniplusprojectapp', '0103_graduatestudysupport'),
    ]

    operations = [
        migrations.CreateModel(
            name='LifeAtUniplusImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='life_at_uniplus/')),
            ],
        ),
    ]