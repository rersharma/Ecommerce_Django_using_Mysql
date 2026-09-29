from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    gender=models.CharField(max_length=10)
    state=models.CharField(max_length=50)
    mobile=models.CharField(max_length=15)
    photo=models.ImageField(upload_to='userphoto/')
    address=models.TextField()
    
    def __str__(self):
        return self.name
    
class help(models.Model):
    subject=models.CharField(max_length=100)
    customer_email=models.EmailField(max_length=100)
    query=models.CharField(max_length=100)
    customer_reply=models.TextField()
    admin_reply=models.TextField()
    
    def __str__(self):
        return self.subject

