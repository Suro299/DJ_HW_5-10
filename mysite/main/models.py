from django.db import models



class Contact(models.Model):
    
    user_name = models.CharField("User Name", max_length = 50)
    user_email = models.EmailField("User Email")
    user_phon = models.CharField("User Phon", max_length = 50)
    user_review = models.TextField("User Review")


    
    def __str__(self):
        return self.user_name
    
    
    
    
class Product(models.Model):
    
    product_name = models.CharField("Product Name", max_length = 50)
    product_price = models.PositiveBigIntegerField("Product Price")
    product_about = models.TextField("Product About", blank = True, default = "")
    product_image = models.ImageField("Product Image", default = "")
    date = models.DateField("Product Data", auto_now = True)

    
    
    def __str__(self):
        return self.product_name