# Generated by Django 4.2.6 on 2024-01-21 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='Family',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='Name',
        ),
    ]
