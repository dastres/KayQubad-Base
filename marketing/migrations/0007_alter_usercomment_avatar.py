# Generated by Django 4.1.5 on 2023-02-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0006_usercomment_company_en_usercomment_company_fa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomment',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='marketing/user_comment/user_comment/avatar/2023/2', verbose_name='avatar'),
        ),
    ]