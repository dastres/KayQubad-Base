# Generated by Django 4.1.5 on 2023-07-28 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_alter_page_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/2023/7', verbose_name='thumbnail'),
        ),
    ]
