# Generated by Django 4.1.5 on 2023-03-05 12:32

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('dastres', '0002_alter_customers_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingSections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_at_jalali', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at_jalali', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('status', models.CharField(choices=[('PU', 'Publish'), ('IN', 'Inriview'), ('PE', 'Pending')], default='PE', max_length=2, verbose_name='status')),
                ('cover_main', models.ImageField(upload_to='landing_sections/cover_main/2023/3', verbose_name='Cover Main')),
                ('title_main_one', models.CharField(max_length=100, verbose_name='Title Main One')),
                ('title_main_one_en', models.CharField(max_length=100, null=True, verbose_name='Title Main One')),
                ('title_main_one_fa', models.CharField(max_length=100, null=True, verbose_name='Title Main One')),
                ('title_main_two', models.CharField(max_length=100, verbose_name='Title Main Two')),
                ('title_main_two_en', models.CharField(max_length=100, null=True, verbose_name='Title Main Two')),
                ('title_main_two_fa', models.CharField(max_length=100, null=True, verbose_name='Title Main Two')),
                ('title_small', models.CharField(max_length=100, verbose_name='Title Small')),
                ('title_small_en', models.CharField(max_length=100, null=True, verbose_name='Title Small')),
                ('title_small_fa', models.CharField(max_length=100, null=True, verbose_name='Title Small')),
                ('title_big', models.CharField(max_length=350, verbose_name='Title Big')),
                ('title_big_en', models.CharField(max_length=350, null=True, verbose_name='Title Big')),
                ('title_big_fa', models.CharField(max_length=350, null=True, verbose_name='Title Big')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('short_description_en', models.TextField(null=True, verbose_name='Short Description')),
                ('short_description_fa', models.TextField(null=True, verbose_name='Short Description')),
                ('link', models.URLField(verbose_name='Link')),
                ('cover_background', models.ImageField(upload_to='landing_sections/cover_background/2023/3', verbose_name='Cover Background')),
                ('cover_video', models.ImageField(upload_to='landing_sections/cover_video/2023/3', verbose_name='Cover Video')),
                ('link_video', models.URLField(verbose_name='Link Video')),
                ('title_one', models.CharField(max_length=100, verbose_name='Title One')),
                ('title_one_en', models.CharField(max_length=100, null=True, verbose_name='Title One')),
                ('title_one_fa', models.CharField(max_length=100, null=True, verbose_name='Title One')),
                ('count_one', models.CharField(max_length=100, verbose_name='Count One')),
                ('count_one_en', models.CharField(max_length=100, null=True, verbose_name='Count One')),
                ('count_one_fa', models.CharField(max_length=100, null=True, verbose_name='Count One')),
                ('title_two', models.CharField(max_length=100, verbose_name='Title Two')),
                ('title_two_en', models.CharField(max_length=100, null=True, verbose_name='Title Two')),
                ('title_two_fa', models.CharField(max_length=100, null=True, verbose_name='Title Two')),
                ('count_two', models.CharField(max_length=100, verbose_name='Count Two')),
                ('count_two_en', models.CharField(max_length=100, null=True, verbose_name='Count Two')),
                ('count_two_fa', models.CharField(max_length=100, null=True, verbose_name='Count Two')),
                ('title_three', models.CharField(max_length=100, verbose_name='Title Three')),
                ('title_three_en', models.CharField(max_length=100, null=True, verbose_name='Title Three')),
                ('title_three_fa', models.CharField(max_length=100, null=True, verbose_name='Title Three')),
                ('count_three', models.CharField(max_length=100, verbose_name='Count Three')),
                ('count_three_en', models.CharField(max_length=100, null=True, verbose_name='Count Three')),
                ('count_three_fa', models.CharField(max_length=100, null=True, verbose_name='Count Three')),
            ],
            options={
                'verbose_name': 'Landing Section',
                'verbose_name_plural': 'Landing Sections',
            },
        ),
    ]
