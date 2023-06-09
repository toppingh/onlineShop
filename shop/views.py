from django.shortcuts import render, get_object_or_404
from . models import *
from cart.forms import AddProductForm

# Create your views here.
# 카테고리 페이지 뷰
def product_in_category(request, category_slug=None): # URL로부터 category_slug를 찾아 현재 어느 카테고리를 보여주는지 판단
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html', {'current_category':current_category, 'categories':categories, 'products':products})

# 제품 상세 뷰
#def product_detail(request, id, product_slug=None):
#    # URL로부터 slug 값을 읽어와 해당 제품을 찾고 그 제품을 노출하는 방식
#    product = get_object_or_404(Product, id=id, slug=product_slug) # 찾는 객체가 없을 경우 자동으로 404페이지를 보여줌
#    return render(request, 'shop/detail.html', {'product':product})

def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart': add_to_cart})