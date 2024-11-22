from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=TRUE)

    def__str___(self):
        return f"{self.first_name} {self.last_name}"