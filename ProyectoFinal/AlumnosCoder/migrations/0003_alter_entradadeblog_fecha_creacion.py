# Generated by Django 4.1.7 on 2023-03-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumnosCoder', '0002_alter_entradadeblog_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradadeblog',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]