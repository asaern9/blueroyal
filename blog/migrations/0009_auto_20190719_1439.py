# Generated by Django 2.2.1 on 2019-07-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190719_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(null=True, upload_to='Pictures/Event'),
        ),
        migrations.AddField(
            model_name='news',
            name='picture',
            field=models.ImageField(null=True, upload_to='Pictures/News'),
        ),
    ]
