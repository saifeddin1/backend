from django.db import models
from classes.models import Classe
# Create your models here.


class Timetable(models.Model):
    content = models.FileField(upload_to='timetables/')
    classe = models.OneToOneField(
        Classe, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Timetable of :'+self.classe.name
