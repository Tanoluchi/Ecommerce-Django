from django.shortcuts import get_object_or_404, render

from .models import Category, Product

def product_all(request):
    products = Product.products.all()

    return render(request, 'store/home.html', {
        'products': products
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)

    return render(request, 'store/products/single.html', {
        'product': product
    })


def category_list(request, category_slug):
    # Traemos un objeto que tenga la categoria que vamos a estar recibiendo.
    category = get_object_or_404(Category, slug=category_slug)
    # Realizamos una lista de productos, filtrando los productos
    # que sean igual a la categoria que recibimos.
    products = Product.objects.filter(category=category)

    return render(request, 'store/products/category.html', {
        'category': category,
        'products': products,
    })