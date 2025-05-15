from django.contrib import admin
from .models import ProductType, Product, Transaction
# Register your models here.


class ProductInLine(admin.TabularInline):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInLine, ]
    search_fields = ('name', )
    list_display = ('name', )
    list_filter = ('name', )


class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ('name', 'product_type', 'price')
    list_display = ('name', 'product_type', 'price', 'stock')
    list_filter = ('name', 'product_type')
    fieldsets = [
        ('Details', {
            'fields': [
                ('name', 'price'), 'product_type'
            ]
        })
    ]

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
