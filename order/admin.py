from django.contrib import admin

# Register your models here.
import csv
import datetime
from django.http import HttpResponse

from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import OrderItem, Order

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename={}.csv'.format(opts.verbose_name)
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # csv 팡리 컬럼 타이틀
    writer.writerow([field.verbose_name for field in fields])

    # 실제 데이터 출력
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%Y-%m-%d")
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'

def order_detail(obj):
    return mark_safe('<a href="{}">Detail</a>'.format(reverse('orders:admin_order_detail', args=[obj.id])))

order_detail.short_description = 'Detail'



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    rqw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display=['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', order_detail, 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]

admin.site.register(Order, OrderAdmin)
