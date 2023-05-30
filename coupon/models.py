from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True) # 쿠폰 사용시 입력하는 코드
    use_from = models.DateTimeField() # 쿠폰 사용 기간
    use_to = models.DateTimeField() # 쿠폰 사용 기간
    amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)]) # 할인금액 0~100000 사이로 설정하는 제약 조건 명시
    active = models.BooleanField() # 사용가능 여부 체크

    def __str__(self):
        return self.code