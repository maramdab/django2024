from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'products.html',context)

def home(request):
    return render(request,'home.html')