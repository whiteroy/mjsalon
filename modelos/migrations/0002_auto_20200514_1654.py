# Generated by Django 3.0.6 on 2020-05-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='telefono',
            field=models.PositiveIntegerField(),
        ),
    ]
