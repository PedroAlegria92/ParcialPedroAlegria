# Generated by Django 3.2.16 on 2022-11-26 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(default='', max_length=64)),
                ('Descripcion', models.CharField(default='', max_length=64)),
                ('Fecha_de_creacion', models.CharField(default='', max_length=64)),
                ('Fecha_de_entrega', models.CharField(default='', max_length=64)),
                ('Usuario_designado', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='', max_length=64)),
                ('Apellido', models.CharField(default='', max_length=64)),
                ('Codigo_de_usuario', models.CharField(default='', max_length=64)),
                ('Clave', models.CharField(default='', max_length=64)),
            ],
        ),
    ]
