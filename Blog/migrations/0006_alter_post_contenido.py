# Generated by Django 4.1.1 on 2022-09-16 13:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_post_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
