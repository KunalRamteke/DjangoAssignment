from django.db import models

# Create your models here.
class Contacts(models.Model):
    FirstName = models.CharField(max_length = 30, blank = True)
    LastName = models.CharField(max_length = 30, blank = False)
    Email = models.EmailField(max_length = 70, blank = False)
    MobileNo = models.DecimalField(max_digits = 10, decimal_places = 0, blank = False)