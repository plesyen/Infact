# Generated by Django 3.1.7 on 2021-03-19 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_fact_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='phrase',
            field=models.CharField(max_length=100),
        ),
    ]