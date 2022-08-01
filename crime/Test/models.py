from django.db import models

# Create your models here.
class AuthUsers(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=10)
    emailid = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    #class Meta:
    #    db_table = "authusers"

    def __str__(self):
        return self.emailid

