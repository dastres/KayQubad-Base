# Generated by Django 4.1.5 on 2023-03-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dastres', '0003_landingsections'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingsections',
            name='is_active_en',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='landingsections',
            name='is_active_fa',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
    ]
