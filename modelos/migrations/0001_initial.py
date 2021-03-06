# Generated by Django 3.0.6 on 2020-05-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('identificacion', models.PositiveIntegerField(unique=True)),
                ('telefono', models.PositiveIntegerField(max_length=50)),
            ],
        ),
    ]
