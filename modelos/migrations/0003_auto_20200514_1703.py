# Generated by Django 3.0.6 on 2020-05-14 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0002_auto_20200514_1654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'managed': True, 'ordering': ['id'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='apellido',
            field=models.CharField(max_length=30, verbose_name='apellido'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='direccion',
            field=models.CharField(max_length=30, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='identificacion',
            field=models.PositiveIntegerField(unique=True, verbose_name='identificacion'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='telefono',
            field=models.BigIntegerField(verbose_name='telefono'),
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table='',
        ),
    ]
