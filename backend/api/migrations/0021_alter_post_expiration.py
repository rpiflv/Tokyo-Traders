# Generated by Django 4.1.5 on 2023-01-24 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_post_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 31, 13, 41, 9, 452909, tzinfo=datetime.timezone.utc)),
        ),
    ]
