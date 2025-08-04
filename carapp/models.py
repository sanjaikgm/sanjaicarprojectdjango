from django.db import models

# Create your models here.
class signuplog(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email_id=models.CharField(max_length=30)
    occupation=models.CharField(max_length=30,default='customer')
class addcarlog(models.Model):
    name=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    img=models.ImageField(upload_to='addimg/')