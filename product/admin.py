from django.contrib import admin
from .models import Category, Product, ProductImages


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 3
    readonly_fields = ('image_icon',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'slug',)
    list_filter = ('status',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_icon', 'title', 'category_tag', 'slug', 'status')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'slug')
    list_filter = ('status',)
    inlines = [ProductImagesInline]
    list_display_links = ('image_icon', 'title')
    
    
@admin.register(ProductImages)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_icon')