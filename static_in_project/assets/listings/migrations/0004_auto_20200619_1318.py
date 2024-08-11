# Generated by Django 3.0.7 on 2020-06-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200619_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='categories',
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
