# Generated by Django 2.2.1 on 2019-07-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190719_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(null=True),
        ),
    ]