from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def products_all(request):
    products = Product.objects.all()[:5]
    # products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'product': product})
