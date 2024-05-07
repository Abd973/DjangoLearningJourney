from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length= 50)
    content = models.TextField()
    price = models.DecimalField(max_digits= 20, decimal_places= 10)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'My_Product'
        ordering = ['name']
    
