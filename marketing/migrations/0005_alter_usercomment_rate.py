# Generated by Django 4.1.5 on 2023-02-25 08:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_alter_usercomment_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomment',
            name='rate',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='rate'),
        ),
    ]