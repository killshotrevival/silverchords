# Generated by Django 2.2.6 on 2019-12-20 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0009_auto_20191221_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='itemcount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
