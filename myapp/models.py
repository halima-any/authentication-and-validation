from django.db import models
from django.contrib.auth.models import AbstractUser

class CUSTOM_USER(AbstractUser):

    USER=[
        ('jobcreator','JOBCREATOR'),
        ('jobseeker','JOBSEEKER')
    ]
    usertype=models.CharField(choices=USER,null=True,max_length=100)

    def __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}"

