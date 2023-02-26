# Generated by Django 4.1.5 on 2023-02-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_study_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='dislike',
            field=models.PositiveIntegerField(default=0, verbose_name='Dislike'),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='like',
            field=models.PositiveIntegerField(default=0, verbose_name='Like'),
        ),
    ]