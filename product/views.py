from django.shortcuts import render
from .models import ProductInfo

# Create your views here.

def product_list(request):
    all_products = ProductInfo.objects.all()
    context = {
        'all_products':all_products
    }
    template_name = 'home.html'
    return render(request, template_name, context)
