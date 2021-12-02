from django.db import models

from classes.models import Classe


class Course(models.Model):
    title = models.CharField(max_length=200)
    content = models.FileField(upload_to='courses/')
    classe = models.ForeignKey(
        Classe, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
