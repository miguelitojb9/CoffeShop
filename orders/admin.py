from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
    
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_active', 'order_date')
    list_filter = ('is_active', 'order_date')
    search_fields = ('user__username',)
    inlines = [OrderProductInline]
    
admin.site.register(Order, OrderAdmin)
