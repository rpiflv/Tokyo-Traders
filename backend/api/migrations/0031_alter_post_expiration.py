# Generated by Django 4.1.4 on 2023-01-25 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_merge_20230125_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 1, 12, 25, 3, 831376, tzinfo=datetime.timezone.utc)),
        ),
    ]
