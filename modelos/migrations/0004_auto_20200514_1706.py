# Generated by Django 3.0.6 on 2020-05-14 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0003_auto_20200514_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='direccion',
            field=models.CharField(max_length=100, verbose_name='direccion'),
        ),
    ]
