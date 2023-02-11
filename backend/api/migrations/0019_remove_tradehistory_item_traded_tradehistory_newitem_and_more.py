# Generated by Django 4.1.4 on 2023-01-21 02:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_post_expiration_tradehistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradehistory',
            name='item_traded',
        ),
        migrations.AddField(
            model_name='tradehistory',
            name='newItem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='newItem', to='api.item'),
        ),
        migrations.AddField(
            model_name='tradehistory',
            name='oldItem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oldItem', to='api.item'),
        ),
        migrations.AlterField(
            model_name='post',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 2, 29, 39, 608481, tzinfo=datetime.timezone.utc)),
        ),
    ]
