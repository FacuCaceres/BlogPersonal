# Generated by Django 4.1.1 on 2022-09-15 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=150, verbose_name='Slug')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripcion')),
                ('imagen', models.URLField(max_length=255)),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('fecha_creacio', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]