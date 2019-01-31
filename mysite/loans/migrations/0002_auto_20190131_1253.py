# Generated by Django 2.1.2 on 2019-01-31 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='loan_amort_months',
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_last_action_date',
            field=models.DateField(default=datetime.date(2019, 1, 31)),
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_payment',
            field=models.DecimalField(decimal_places=2, default=350, max_digits=6),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_start_date',
            field=models.DateField(default=datetime.date(2019, 1, 31)),
        ),
    ]
