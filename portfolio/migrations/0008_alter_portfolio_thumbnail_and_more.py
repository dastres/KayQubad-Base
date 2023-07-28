# Generated by Django 4.1.5 on 2023-07-28 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_portfolio_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/2023/7', verbose_name='thumbnail'),
        ),
        migrations.AlterField(
            model_name='portfoliocategory',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='taxonomy/thumbnails/2023/7', verbose_name='thumbnail'),
        ),
        migrations.AlterField(
            model_name='portfoliogallery',
            name='image',
            field=models.ImageField(upload_to='basic_gallery/images/2023/7', verbose_name='image'),
        ),
    ]
