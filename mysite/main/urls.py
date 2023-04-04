from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_request, name='login'),
    # path('register/',views.register_request, name='register'),
    path("logout", views.logout_request, name='logout'),
    
    path("home/", views.home, name = "home"),
    path("contact/", views.contact, name = "contact"),
    path("review/", views.review, name = "review"),
    path("shop/", views.shop, name = "shop"),
    path("product/<int:id>/", views.shop_detail, name = "shop_detail"),
    path("add_to_shop/", views.add_to_shop, name = "add_to_shop"),
    
    path("ftf/", views.ftf, name = "ftf")
]
