# Generated by Django 4.1.5 on 2023-03-25 17:42

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_at_jalali', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at_jalali', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('is_active_en', models.BooleanField(default=False, verbose_name='is active')),
                ('is_active_fa', models.BooleanField(default=False, verbose_name='is active')),
                ('meta_title', models.CharField(blank=True, max_length=320, null=True, verbose_name='meta title')),
                ('meta_description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='meta description')),
                ('status', models.CharField(choices=[('PU', 'Publish'), ('IN', 'Inriview'), ('PE', 'Pending')], default='PE', max_length=2, verbose_name='status')),
                ('title', models.CharField(max_length=350, verbose_name='title')),
                ('title_en', models.CharField(max_length=350, null=True, verbose_name='title')),
                ('title_fa', models.CharField(max_length=350, null=True, verbose_name='title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content')),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content')),
                ('content_fa', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/2023/3', verbose_name='thumbnail')),
                ('thumbnail_alt', models.CharField(blank=True, max_length=350, verbose_name='thumbnail alt')),
                ('short_description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Short Description')),
                ('short_description_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Short Description')),
                ('short_description_fa', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Short Description')),
                ('position', models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], default='Left', max_length=5, verbose_name='Position')),
                ('is_landing', models.BooleanField(default=False, verbose_name='is Landing ?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
