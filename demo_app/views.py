from django.shortcuts import render,redirect
from django.http import HttpResponse 
from . models import Product
from . forms import *
from django.contrib import messages


# Create your views here.
def index(request):
    return HttpResponse('this is from the demo app')

def test(request):
    HttpResponse('this is a demo app')
    
def show_product(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'demo/index.html',context)

def post_category(request):
    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category added successfully')
            return redirect('/demo/addcategory')
        else:
            messages.add_message(request,messages.ERROR,'Please verify field form')
        return render(request,'demo/addcategory.html', {
            'form':form
        })    
                     
    context={
            'form': CategoryForm
      }
    return render(request,'demo/addcategory.html',context)

def post_product(request):
    if request.method == 'POST':
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'product added successfully')
            return redirect('/demo/addproduct')
        else:
            messages.add_message(request,messages.ERROR,'Please verify field form')
            return render(request,'demo/addproduct.html', {
            'form':form
        })    
                     
    context={
            'form': ProductForm
      }
    return render(request, 'demo/addproduct.html',context)


