# Generated by Django 2.1.7 on 2019-06-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portada', '0004_portada_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portada',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
