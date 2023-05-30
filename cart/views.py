from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .forms import AddProductForm
from .cart import Cart

from coupon.forms import AddCouponForm

# Create your views here.
@require_POST # 로그인을 했을때만 사용할 수 있도록 제한함!
# 카트에 제품 추가, 추가하는 제품의 정보는 상세페이지나 장바구니 페이지로부터 전달됨
def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = AddProductForm(request.POST) # AddProductForm을 통해 만들어진 데이터!

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])

    return redirect('cart:detail')

# 카트에서 제품 삭제
def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')

# 장바구니 페이지
def detail(request):
    cart = Cart(request)
    add_coupon = AddCouponForm()

    # AddProductForm을 제품마다 하나씩 추가(노출될 제품을 카트로부터 가져오는데 제품 수량 수정을 위함)
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity':product['quantity'], 'is_update':True})
        # 수량은 수정하는대로 반영해야하므로 is_update = True로 설정
    return render(request, 'cart/detail.html', {'cart':cart, 'add_coupon':add_coupon})