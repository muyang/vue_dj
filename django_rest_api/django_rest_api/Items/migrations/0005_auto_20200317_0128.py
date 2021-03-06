# Generated by Django 3.0.4 on 2020-03-17 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0004_auto_20200316_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_location',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_rotation',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.UUIDField(default=0),
            preserve_default=False,
        ),
    ]
