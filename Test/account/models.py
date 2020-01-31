from django.db import models
from phone_field import PhoneField
# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)
    Date_Of_Birth = models.DateField()
    Mobile_Number = PhoneField(help_text='Contact Phone NUmber')

    def __str__(self):
        return f'{self.Name}'