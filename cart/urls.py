from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns=[
    path('', detail, name='detail'),
    path('add/<int:product_id>', add, name='product_add'), # product_id에 해당하는 제품을 추가
    path('remove/<product_id>', remove, name='product_remove'), # product_id에 해당하는 제품 삭제
]