from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('test/',views.test),    
    path('product/',views.show_product),
    path('addcategory/',views.post_category),
    path('addproduct/',views.post_product),
    ]
