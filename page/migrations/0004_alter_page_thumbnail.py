# Generated by Django 4.1.5 on 2023-04-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_page_is_active_alter_page_is_active_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/2023/4', verbose_name='thumbnail'),
        ),
    ]
