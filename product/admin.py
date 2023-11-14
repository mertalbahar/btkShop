from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'slug',)
    list_filter = ('status',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_tag', 'slug', 'status')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'slug')
    list_filter = ('status',)