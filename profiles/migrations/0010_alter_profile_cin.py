# Generated by Django 3.2.9 on 2021-12-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20211201_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cin',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
