from django.contrib import admin
from.models import Customer,Card,OrderPlaced,Product

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','product_image']

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status']
