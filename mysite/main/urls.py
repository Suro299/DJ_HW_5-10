from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("contact/", views.contact, name = "contact"),
    path("review/", views.review, name = "review"),
    path("shop/", views.shop, name = "shop"),
    path("add_to_shop/", views.add_to_shop, name = "add_to_shop"),
    
    path("ftf/", views.ftf, name = "ftf")
]
