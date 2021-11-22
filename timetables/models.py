from django.db import models

# Create your models here.


class Timetable(models.Model):
    content = models.FileField(upload_to='timetables/');


    

