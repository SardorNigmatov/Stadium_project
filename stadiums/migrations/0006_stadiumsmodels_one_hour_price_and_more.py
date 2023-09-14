# Generated by Django 4.2.5 on 2023-09-14 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadiums', '0005_alter_bronmodel_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadiumsmodels',
            name='one_hour_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='bronmodel',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2023, 9, 14, 16, 10, 12, 141293)),
        ),
    ]