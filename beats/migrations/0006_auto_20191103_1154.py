# Generated by Django 2.2.6 on 2019-11-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0005_auto_20191103_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[('1', 'Poor'), ('2', 'Ok Ok'), ('3', 'Average'), ('4', 'Great'), ('5', 'Blast')], default=5),
        ),
    ]
