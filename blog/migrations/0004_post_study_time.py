# Generated by Django 4.1.5 on 2023-02-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_short_description_post_short_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='study_time',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='study time'),
        ),
    ]