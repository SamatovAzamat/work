# Generated by Django 3.2 on 2021-06-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familiya', models.CharField(max_length=100)),
                ('ism', models.CharField(max_length=100)),
                ('ty', models.IntegerField()),
            ],
        ),
    ]
