from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    dept = models.CharField(max_length=100)


    def __str__(self):
      return self.name + " " + self.dept
  
  