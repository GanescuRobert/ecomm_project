from sre_parse import State
from django.db import models
from django.contrib.auth.models import User

import datetime
import os

from phonenumber_field.modelfields import PhoneNumberField


def get_file_path(request, filename):
    original_filename = filename
    now_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (now_time, original_filename)
    return os.path.join('uploads/', filename)


class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(
        default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(
        default=False, help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(
        max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(
        upload_to=get_file_path, null=True, blank=True)
    small_description = models.CharField(
        max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(
        default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(
        default=False, help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(
        max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
class Order(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
     
    # Contact details
    email = models.EmailField(max_length=70, blank=True,unique=False)
    phone = PhoneNumberField(null=False, blank=False, unique=False)
    # Address details
    
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    zipcode = models.CharField(max_length=150, null=False)
    # Other details
    details =  models.TextField(null=False)
    
    # Order summary
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150,null=False)
    payment_id = models.CharField(max_length=250, null=True)
    
    order_statuses = (
        ("Pending","Pending"),
        ("Out for Shipping","Out for Shipping"),
        ("Completed","Completed")
    )
    
    status = models.CharField(max_length=150,choices=order_statuses, default="Pending")
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)
    
    def get_full_address(self):
        return ', '.join([self.city, self.state, self.country, self.zipcode, self.details]) 
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    
    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_no)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    zipcode = models.CharField(max_length=150, null=False)
    details =  models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username