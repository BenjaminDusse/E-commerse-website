from django.shortcuts import get_object_or_404, render
from cart.forms import CartAddProductForm
from onlineshop.models import Category, Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    print(products)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'onlineshop/product/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    
    context = {
        'product': product,
        'cart_product_form': cart_product_form,

    }
    return render(request, 'onlineshop/product/detail.html', context)    


