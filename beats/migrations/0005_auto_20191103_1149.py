# Generated by Django 2.2.6 on 2019-11-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0004_auto_20191103_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.PositiveSmallIntegerField(default=5, max_length=5),
        ),
    ]
