# Generated by Django 4.1.5 on 2023-04-03 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_alter_contactus_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='created_at_jalali',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='updated_at_jalali',
        ),
    ]