# Generated by Django 3.1.6 on 2021-03-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homebudget', '0018_auto_20210313_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='timestamp',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='timestamp',
            field=models.DateField(),
        ),
    ]