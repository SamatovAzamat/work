# Generated by Django 3.2 on 2021-06-08 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ism',
            name='qoshilgan_sanasi',
            field=models.DateTimeField(auto_now=True),
        ),
    ]