# Generated by Django 4.1.7 on 2023-03-22 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaDeBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_entrada', models.CharField(max_length=50)),
                ('subtitulo_entrada', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
