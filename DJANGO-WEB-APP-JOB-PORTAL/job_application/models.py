from django.db import models

# Create your models here.
class Form(models.Model):
    first_name = models.CharField(max_length=80, null=False)
    last_name = models.CharField(max_length=80, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True, )
    date = models.DateField(null=False,)
    occupation = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"