# Generated by Django 4.1.5 on 2023-03-05 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='status_en',
        ),
        migrations.RemoveField(
            model_name='service',
            name='status_fa',
        ),
    ]