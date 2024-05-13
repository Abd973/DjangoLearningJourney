from django.db import models

# Create your models here.

class Female(models.Model):
    name_female = models.CharField(max_length=40, null=False)
    def __str__(self):
        return self.name_female

class Male(models.Model):
    name_male = models.CharField(max_length=40, null=False)
    females = models.OneToOneField(Female, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_male
    


class Product(models.Model):
    title = models.CharField(max_length=40, null=False)
    def __str__(self):
        return self.name_male


class User(models.Model):
    name = models.CharField(max_length=40, null=False)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_male
