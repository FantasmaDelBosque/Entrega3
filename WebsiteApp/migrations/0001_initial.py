# Generated by Django 4.2.4 on 2023-09-17 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conciertos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('lugar', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('boton_compra', models.URLField(blank=True)),
            ],
        ),
    ]