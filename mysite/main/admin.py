from django.contrib import admin
from .models import Contact, Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "user_email")
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "product_price")
    