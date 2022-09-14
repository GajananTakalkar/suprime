from django.db import models

class Contacts(models.Model):
    name = models.CharField( max_length=50,null=True)
    Addr=models.CharField(max_length=50,null=True)
    mobile = models.CharField( max_length=50,null=True)
    mail=models.CharField(max_length=50,null=True)
    Inquiry=models.CharField(max_length=500,null=True)