# Generated by Django 2.2.1 on 2019-07-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190719_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(verbose_name='%d %B, %Y'),
        ),
    ]
