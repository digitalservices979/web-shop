# Generated by Django 2.1.7 on 2019-05-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190517_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prenda',
            name='imagen',
            field=models.ImageField(upload_to='projects'),
        ),
    ]