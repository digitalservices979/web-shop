# Generated by Django 2.1.7 on 2019-05-17 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prenda',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
