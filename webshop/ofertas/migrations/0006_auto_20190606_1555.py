# Generated by Django 2.1.7 on 2019-06-06 20:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0005_auto_20190606_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofertas',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]