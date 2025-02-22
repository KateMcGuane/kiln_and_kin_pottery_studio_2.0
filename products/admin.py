from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'stock',
        'material',
        'glaze_type',
        'colour',
        'height',
        'opening_diameter',
        'diameter_at_widest_point',
        'base_diameter',
        'weight',
        'capacity',
        'image',
    )
    
    ordering = ('sku',)
    
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)