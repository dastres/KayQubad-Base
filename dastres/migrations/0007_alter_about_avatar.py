# Generated by Django 4.1.5 on 2023-04-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dastres', '0006_remove_about_social_media_socialmedia_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='dastres/about/avatar/2023/4', verbose_name='avatar'),
        ),
    ]
