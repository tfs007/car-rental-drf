# Generated by Django 3.0 on 2021-05-20 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20210520_0622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carbooking',
            old_name='Cardropoff_date',
            new_name='cardropoff_date',
        ),
        migrations.RenameField(
            model_name='carbooking',
            old_name='Carpickup_date',
            new_name='carpickup_date',
        ),
    ]
