from django.contrib import admin
from .models import ProductType, Product
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
    list_display = ('name', 'product_type', 'price')
    list_filter = ('name', 'product_type')
    fieldsets = [
        ('Details', {
            'fields': [
                ('name', 'price'), 'product_type'
            ]
        })
    ]


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
