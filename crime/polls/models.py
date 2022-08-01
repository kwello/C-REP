from django.db import models

class auth_users(models.Model):
    name=models.CharField(max_length=20),
    mob_no=models.CharField(max_length=10),
    emailid=models.CharField(max_length=15),
    date=models.DateField(),
    country=models.CharField(max_length=15),
    state=models.CharField(max_length=15),
    district=models.CharField(max_length=15),
    crime=models.CharField(max_length=15),
    complain=models.CharField(max_length=500)

    def __str__(self):
        return self.emailid
