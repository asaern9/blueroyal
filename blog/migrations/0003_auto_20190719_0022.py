# Generated by Django 2.2.1 on 2019-07-19 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190719_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='adult',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1),
        ),
    ]
