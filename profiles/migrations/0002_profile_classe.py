# Generated by Django 3.2.9 on 2021-12-01 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='classe',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='classes.classe'),
            preserve_default=False,
        ),
    ]
