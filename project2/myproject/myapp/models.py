from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    designation = models.CharField(max_length=50)
    joining_date = models.DateField()

    def __str__(self):
        return self.name
