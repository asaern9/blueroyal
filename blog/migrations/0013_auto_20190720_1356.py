# Generated by Django 2.2.1 on 2019-07-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190720_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='adult',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1),
        ),
    ]
