# Generated by Django 5.1.2 on 2024-11-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_rename_descripcion_tarea_integrantes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='justificacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
