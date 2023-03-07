from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from django.dispatch import receiver
from django.forms import ImageField, IntegerField
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.


class Product(models.Model):
    product_id=models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product/images")

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    phone =models.CharField(max_length=50)
    address= models.TextField(max_length=500)
    products= models.ManyToManyField(Product)
    order_date= models.DateField( )
    # price = models.IntegerField()

    def __str__(self):
        print(self.order_id)
        return str(self.order_id)

class Plan(models.Model):
    plan_id=models.BigAutoField(primary_key=True)
    plan_name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=500)
    plan = models.TextField()
    image = models.ImageField(upload_to="plan/images")

    def __str__(self):
        return self.plan_name

class Blog(models.Model):
    blog_id=models.BigAutoField(primary_key=True)
    blog_name = models.CharField(max_length=50)
    desc = models.TextField()
    likes = models.IntegerField()
    image = models.ImageField(upload_to="blog/images")

    def __str__(self):
        return self.blog_name