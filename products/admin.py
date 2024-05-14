from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'category']
    list_editable = ['active', 'category']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.site_header = 'Abdulmalik panel'
admin.site.site_title = 'Admin panel'
