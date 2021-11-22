from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cin = models.IntegerField()
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
