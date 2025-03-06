from django.db import models

# Create your models here.
class people_table(models.Model):
    id = models.IntegerField(primary_key=True)
    Full_name = models.CharField(max_length=100, verbose_name="Full Name")
    Father_name = models.CharField(max_length=100, verbose_name="Father Name")
    Mother_name = models.CharField(max_length=100, verbose_name="Mother Name")
    address = models.CharField(max_length=100, verbose_name="Address")
    Age = models.IntegerField()
    Blood_group = models.CharField(max_length=100, verbose_name="Blood Group", null=True)

def __str__(self):
    return f"{self.id} : {self.Full_name}"

