# Generated by Django 2.1.7 on 2019-05-31 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portada', '0002_auto_20190531_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portada',
            old_name='image',
            new_name='imagen',
        ),
    ]
