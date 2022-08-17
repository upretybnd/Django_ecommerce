from django.forms import ModelForm,fields

from .models import *

class CategoryForm(ModelForm):
    class Meta:
        model=category
        fields="__all__"
        
        
class ProductForm(ModelForm):
    class Meta:
        model =Product
        fields ='__all__'

