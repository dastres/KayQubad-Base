# Generated by Django 4.1.5 on 2023-02-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_thumbnail_alter_postcategory_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.CharField(max_length=50, null=True, verbose_name='Short Discription'),
        ),
        migrations.AddField(
            model_name='post',
            name='short_description_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Short Discription'),
        ),
        migrations.AddField(
            model_name='post',
            name='short_description_fa',
            field=models.CharField(max_length=50, null=True, verbose_name='Short Discription'),
        ),
    ]
