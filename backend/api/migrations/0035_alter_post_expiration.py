# Generated by Django 4.1.4 on 2023-01-27 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_alter_item_category_alter_post_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 12, 25, 59, 472662, tzinfo=datetime.timezone.utc)),
        ),
    ]
