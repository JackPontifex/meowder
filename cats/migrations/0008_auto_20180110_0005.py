# Generated by Django 2.0.1 on 2018-01-10 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0007_auto_20180110_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='pic1',
            field=models.URLField(null=True, verbose_name='picture 1'),
        ),
    ]
