# Generated by Django 3.1.6 on 2021-03-13 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homebudget', '0008_auto_20210313_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 13, 10, 40, 58, 330589)),
        ),
        migrations.AlterField(
            model_name='income',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 13, 10, 40, 58, 330920)),
        ),
    ]
