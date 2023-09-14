# Generated by Django 4.2.5 on 2023-09-14 06:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StadiumsModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('contact', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('img', models.ImageField(blank=True, null=True, upload_to='news/')),
                ('stadium_about', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'stadiums',
            },
        ),
    ]
