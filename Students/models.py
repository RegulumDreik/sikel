from django.db import models


# Create your models here.
class StudentModel(models.Model):
    first_name = models.CharField(max_length=32, blank=False)
    middle_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=False)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=False)

    def __str__(self):
        return self.first_name+self.last_name