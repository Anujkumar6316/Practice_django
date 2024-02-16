from django.db import models

# Create your models here.
class Id_details(models.Model):
    # img = models.ImageField(upload_to='images/')
    uid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name