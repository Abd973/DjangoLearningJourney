from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
    x = [
        ('Phone', 'Phone'),
        ('Headphone', 'Headphone')
    ]

    name = models.CharField(max_length= 50)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits= 20, decimal_places= 10)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=False)
    category = models.CharField(max_length=20, null= True, blank=True, choices=x)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'My_Product'
        ordering = ['price']
    
class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    DT = models.DateTimeField(default=datetime.now)
