# Generated by Django 2.1.7 on 2019-06-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ofertas',
            fields=[
                ('id_oferta', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('asunto', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('destinatarios', models.IntegerField()),
                ('fecha_envio', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Ofertas',
                'db_table': 'ofertas',
                'ordering': ['-fecha_envio'],
            },
        ),
    ]
