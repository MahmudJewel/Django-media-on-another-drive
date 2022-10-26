from django.shortcuts import render, redirect
from .models import ProductInfo
from .forms import ProductInfoForm
# Create your views here.


def product_list(request):
    template_name = 'home.html'
    all_products = ProductInfo.objects.all()
    context = {
        'all_products': all_products
    }
    return render(request, template_name, context)


def product_view(request, pk):
    template_name = 'product_view.html'
    product = ProductInfo.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, template_name, context)


def create_product(request):
    template_name = 'product_create.html'
    productForm = ProductInfoForm()
    if request.method == 'POST':
        productForm = ProductInfoForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
            print('Product form=> ', productForm)
            return redirect("/")
    context = {
        'productForm': productForm
    }
    return render(request, template_name, context)


def update_product(request, pk):
    template_name = 'update_product.html'
    product = ProductInfo.objects.get(id=pk)
    productForm = ProductInfoForm(instance=product)
    if request.method == 'POST':
        productForm = ProductInfoForm(request.POST, request.FILES, instance=product)
        if productForm.is_valid():
            productForm.save()
            # print('Product form=> ', productForm)
            return redirect("/")
    context = {
        'productForm': productForm,
        'product':product
    }
    return render(request, template_name, context)
