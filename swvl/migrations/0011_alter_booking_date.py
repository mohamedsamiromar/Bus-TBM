# Generated by Django 3.2.3 on 2021-06-27 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swvl', '0010_alter_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 27, 19, 46, 43, 985722)),
        ),
    ]
