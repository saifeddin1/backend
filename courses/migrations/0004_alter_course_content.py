# Generated by Django 3.2.9 on 2021-11-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='content',
            field=models.FileField(upload_to='file_uploads/'),
        ),
    ]