from django.shortcuts import render, redirect
from .forms import ContactModelForm, ProductModelForm
from .models import Contact, Product
from django.db.models import Q


def home(request):
    return render(request, "main/home.html")


def ftf(request):
    return render(request, "main/ftf.html")


def review(request):
    review_list = Contact.objects.all()
    
    return render(request, "main/review.html", context = {
        "review_list":review_list[::-1]
    })

def contact(request):
    res = "\n\n"
    res_color = "rgba(255, 0, 0, 0.782)"
    res_text_shadow = "0 0 5px rgba(255, 0, 0, 0.607)"
    
    if request.method == "POST":
        fields = ContactModelForm(request.POST)  
              
        if fields.is_valid():
            Contact.objects.create(**fields.cleaned_data)
            
            res = "Uxarkvac e"
            res_color = "rgba(0, 255, 26, 0.607)"
            res_text_shadow = "0 0 5px rgba(0, 255, 26, 0.607)"
            
            redirect("contact")
        else:
            res = "Stugeq inputnery"     
        
    else:
        fields = ContactModelForm()
         
    return render(request, "main/contact.html", context = {"fields": fields, "res": res, "res_color": res_color, "res_text_shadow": res_text_shadow})




def shop(request):
    products_list = Product.objects.all()
    search_post = request.GET.get("search")
    
    if search_post:
        products_list = Product.objects.filter(Q(product_name__icontains=search_post) | Q(product_price__icontains=search_post))
        
    return render(request, "main/shop.html", context = {"products_list": products_list})



def add_to_shop(request):
    res = "\n\n"
    res_color = "rgba(255, 0, 0, 0.782)"
    res_text_shadow = "0 0 5px rgba(255, 0, 0, 0.607)"
    
    if request.method == "POST":
        fields = ProductModelForm(request.POST, request.FILES)
        if fields.is_valid():
            Product.objects.create(**fields.cleaned_data)
            
            res = "Uxarkvac e"
            res_color = "rgba(0, 255, 26, 0.607)"
            res_text_shadow = "0 0 5px rgba(0, 255, 26, 0.607)"
            
            redirect("add_to_shop")
        else:
            res = "Stugeq inputnery"
    else:
        fields = ProductModelForm()
     
    return render(request, "main/add_to_shop.html", context = {
        "fields": fields, 
        "res": res, 
        "res_color": res_color, 
        "res_text_shadow": res_text_shadow
        })
        
        

def shop_detail(request, id):
    one_product = Product.objects.get(pk=id)
    
    return render(request, "main/shop_detail.html", context = {
        "one_product": one_product
    })