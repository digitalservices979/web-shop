# Generated by Django 2.1.7 on 2019-06-01 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_mensajes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensajes',
            options={'ordering': ['-fecha_creacion'], 'verbose_name_plural': 'Mensajes'},
        ),
    ]
