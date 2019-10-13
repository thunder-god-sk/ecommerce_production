from django.contrib import admin
from .models import Product, ProductImage, Variations
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy  = 'timestamp'
    search_fields = ['title','description']
    list_display = ['title', 'price', 'active', 'updated']
    list_editable = ['price', 'active']
    list_filter = ['price', 'updated']
    readonly_fields = ['timestamp','updated']
    prepopulated_fields = {'slug':('title',)}
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Variations)
