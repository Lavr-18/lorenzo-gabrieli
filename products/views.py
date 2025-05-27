from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        selected_category = get_object_or_404(Category, pk=category_id)
        products = Product.objects.filter(category=selected_category)
    else:
        selected_category = None
        products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': category,
    })
