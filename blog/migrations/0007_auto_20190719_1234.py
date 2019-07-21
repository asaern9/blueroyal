# Generated by Django 2.2.1 on 2019-07-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time_end',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time_start',
            field=models.DateTimeField(null=True),
        ),
    ]