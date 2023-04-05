from django.shortcuts import render, redirect
from .forms import ContactModelForm, ProductModelForm
from .models import Contact, Product
from django.db.models import Q
from django.views.generic import ListView
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def register_request(request):
    res = "\n\n "
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        else:
            res = "Unsuccessful registration. Invalid information."
            messages.error(request, "Unsuccessful registration. Invalid information.")
            return render(request=request, template_name="main/register.html", context={"register_form":form, "res":res})
            
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form":form, "res":res})


def login_request(request):
    res = "\n\n "
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                res = "Invalid username or password."
                messages.error(request,"Invalid username or password.")
                return render(request=request, template_name="main/login.html", context={"login_form":form, "res": res})
                
        else:
            res = "Invalid username or password."
            messages.error(request,"Invalid username or password.")
            return render(request=request, template_name="main/login.html", context={"login_form":form, "res": res})
          
    form = AuthenticationForm()
 
    return render(request=request, template_name="main/login.html", context={
        "login_form":form,
        "res": res
        
    })

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")


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
    
    if request.method == "POST":
        id_delete = request.POST.get("id_delete")
        id_edit = request.POST.get("id_edit")
        
        if id_delete != None:
            prod = Product.objects.get(id = id_delete)
            prod.delete()
            
    search_post = request.GET.get("search")
    products_list = Product.objects.all()
    
    
    
    if search_post:
        products_list = products_list.filter(Q(product_name__icontains=search_post) | Q(product_price__icontains=search_post))
        
    return render(request, "main/shop.html", context={"products_list": products_list})

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