# Generated by Django 3.2 on 2021-06-15 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210615_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read',
            field=models.IntegerField(default=0),
        ),
    ]
