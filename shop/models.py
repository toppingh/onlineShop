from django.db import models
from django.urls import reverse

# Create your models here.
# Category 클래스
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)

    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True)

    class Meta:
        ordering =['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])

# Product 클래스
class Product(models.Model):
    # ForeignKey로 카테고리 참조, SET_NULL => 카테고리가 삭제될 가능성이 있으믈 상품은 남아야하니까 카테고리값을 널 값으로 => null=True
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    # 카테고리와 상품 모두에 설정되는데 상품명 등을 이용해서 URL을 만드는 방식임 . 많은 블로그와 쇼핑몰에서 사용하는 방식으로 SEO에 도움이 되는 URL을 만들 수 있음
    # slug => URL 구성요소로 웹 사이트 특정 페이지를 가리키는 사람이 읽기 쉬운 형식의 식별자

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])