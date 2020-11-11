# Generated by Django 3.1.3 on 2020-11-09 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201109_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='station_type',
        ),
        migrations.AddField(
            model_name='station',
            name='station_type',
            field=models.ManyToManyField(blank=True, to='api.Station_type', verbose_name='Tipo de estacion'),
        ),
    ]