# Generated by Django 4.1.5 on 2023-02-26 11:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_postcomment_dislike_postcomment_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='like',
        ),
        migrations.AddField(
            model_name='postcomment',
            name='likes',
            field=models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL, verbose_name='Likes'),
        ),
        migrations.RemoveField(
            model_name='postcomment',
            name='dislike',
        ),
        migrations.AddField(
            model_name='postcomment',
            name='dislike',
            field=models.ManyToManyField(related_name='dislike_comments', to=settings.AUTH_USER_MODEL, verbose_name='Dislikes'),
        ),
    ]