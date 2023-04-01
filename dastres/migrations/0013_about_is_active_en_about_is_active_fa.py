# Generated by Django 4.1.5 on 2023-04-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dastres', '0012_about_description_en_about_description_fa'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='is_active_en',
            field=models.IntegerField(choices=[(1, 'ACTIVE'), (0, 'INACTIVE')], default=0, null=True, verbose_name='is active ?'),
        ),
        migrations.AddField(
            model_name='about',
            name='is_active_fa',
            field=models.IntegerField(choices=[(1, 'ACTIVE'), (0, 'INACTIVE')], default=0, null=True, verbose_name='is active ?'),
        ),
    ]
