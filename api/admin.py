from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Order, Cart, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock', 'category']
    list_filter = ['category']
    search_fields = ['name', 'description']


admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)