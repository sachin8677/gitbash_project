from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to="category",blank=True,default='')

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to="category",blank=True,default='')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)
