from django.db import models

class Admin(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='productphoto/')
    description=models.TextField()
    
    def __str__(self):
        return self.name
    
class Product_order(models.Model):
    customer_email=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    qnty=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    photo=models.TextField()
    description=models.TextField()
    def __str__(self):
            return self.customer_email
    
        
        