# Generated by Django 3.1.7 on 2021-03-21 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210320_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='popularity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fact',
            name='phrase',
            field=models.CharField(max_length=1000),
        ),
    ]