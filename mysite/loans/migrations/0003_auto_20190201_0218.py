# Generated by Django 2.1.2 on 2019-02-01 02:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_auto_20190131_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_last_action_date',
            field=models.DateField(default=datetime.date(2019, 2, 1)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_start_date',
            field=models.DateField(default=datetime.date(2019, 2, 1)),
        ),
    ]