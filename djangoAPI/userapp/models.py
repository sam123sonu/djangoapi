from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    company_name = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    zip = models.IntegerField()
    email = models.CharField(max_length=500)
    web = models.CharField(max_length=500)
    age = models.IntegerField()