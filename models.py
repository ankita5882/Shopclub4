from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MaxLengthValidator

# Register your models here.
STATE_CHOICE =(
    ('Andman & Nicobar','Andman & Nicobar'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Assam','Assam'),
    ('bihar','bihar'),
    
)
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city= models.CharField(max_length=60)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICE , max_length=60)
    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','laptop'),
    ('TW','top Wear'),
    ('BW','Bottom wear'),
    ('Other','other')
)

class Product(models.Model):
    title=models.CharField(max_length=200)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField( choices=CATEGORY_CHOICES, max_length=5)
    product_image=models.ImageField(upload_to='producting')
    def __str__(self):
        return str(self.id)


class Card(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)

STATUS=(
    ('Order palaced','Order palaced'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Deliverd'),
    ('Out For Delevery','Out For Delevery'),
  
    ('Cancel' ,'Cancel'),

)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=STATUS,default='Order_palaced')
    def __str__(self):
        return str(self.id)

# class cod(models.Model):
#     cass_on=models.models.BinaryField(_(""))


