# Generated by Django 5.1.2 on 2024-10-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_tarea_fecha_alter_tarea_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='hora',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
