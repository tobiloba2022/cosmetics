from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Product
# Create your models here.


class Shopcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    amount = models.FloatField(default=1.0)
    cart_no = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'shopcart'
        managed = True
        verbose_name = 'shopcart'
        verbose_name_plural = 'shopcarts'


STATUS = [
    ('New', 'New'),
    ('Processing', 'Processing'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled')
]

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField(default=1.0)
    cart_no = models.CharField(max_length=50)
    pay_code = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length= 50, choices=STATUS, default= 'NEW')
    created = models.DateField(auto_now_add=True)
    admin_note = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


    class Meta:
        db_table = 'payment'
        managed = True
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'    

class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    billing_address = models.CharField(max_length=250)
    delivery_address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)


    def __str__(self):
        return self.user.username


    class Meta:
        db_table = 'shipping'
        managed = True
        verbose_name = 'Shipping'
        verbose_name_plural = 'Shippings'