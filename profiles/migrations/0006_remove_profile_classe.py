# Generated by Django 3.2.9 on 2021-12-01 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_classe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='classe',
        ),
    ]
