# Generated by Django 3.2.3 on 2021-07-11 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swvl', '0014_alter_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 11, 20, 0, 40, 30374)),
        ),
    ]