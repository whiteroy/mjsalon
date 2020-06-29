# Generated by Django 3.0.6 on 2020-05-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0004_auto_20200514_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre')),
                ('direccion', models.CharField(max_length=100, verbose_name='direccion')),
                ('ciudad', models.CharField(max_length=100, verbose_name='ciudad')),
                ('telefono', models.BigIntegerField(verbose_name='telefono')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('paginaweb', models.URLField(verbose_name='paginaweb')),
                ('mision', models.TextField(verbose_name='mision')),
                ('vision', models.TextField(verbose_name='vision')),
                ('objetivos', models.TextField(verbose_name='objetivos')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
