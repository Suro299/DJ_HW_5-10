from django import forms
from .models import Contact, Product

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return 


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["user_name", "user_email", "user_phon", "user_review"]
        
        
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_price", "product_about", "product_image"]