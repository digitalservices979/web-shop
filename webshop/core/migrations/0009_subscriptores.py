# Generated by Django 2.1.7 on 2019-06-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190603_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriptores',
            fields=[
                ('id_subscriptor', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.TextField()),
                ('fecha_subscripcion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'subscriptores',
            },
        ),
    ]
