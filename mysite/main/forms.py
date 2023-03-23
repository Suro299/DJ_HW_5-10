from django import forms
from .models import Contact, Product




class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["user_name", "user_email", "user_phon", "user_review"]
        
        
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_price", "product_about", "product_image"]