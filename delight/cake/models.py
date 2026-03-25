from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = (
        ('cake', 'Cake'),
        ('drink', 'Drink'),
        ('snacks', 'Snacks'),
    )
    
   
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
    
    # contact form
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    message=models.TextField()  
   
    def __str__(self):
        return self.name

