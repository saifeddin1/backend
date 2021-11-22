from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    content = models.FileField(upload_to='courses/')

    
    def __str__(self):
        return self.title 


