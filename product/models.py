from django.db import models
from django.utils.text import slugify
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    title = models.CharField(max_length=30, verbose_name='Kategori')
    keywords = models.CharField(max_length=250, verbose_name='Anahtar Kelime')
    description = models.TextField(verbose_name='Açıklama')
    image = models.ImageField(blank=True, upload_to='images/', verbose_name='Resim')
    status = models.CharField(max_length=10, choices=STATUS, default=False, verbose_name='Yayınla')
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme')
    
    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
    
    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Ürün')
    keywords = models.CharField(max_length=250, verbose_name='Anahtar Kelime')
    description = models.TextField(verbose_name='Açıklama')
    image = models.ImageField(blank=True, upload_to='images/', verbose_name='Resim')
    price = models.FloatField(verbose_name='Birim Fiyat')
    amount = models.IntegerField(default=0, verbose_name='Adet')
    detail = models.TextField(verbose_name='Detay')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='Yayınla')
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme')
    
    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def category_tag(sef):
        return sef.category
    
    category_tag.short_description = 'Kategori'
    
    def image_icon(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    
    image_icon.short_description = 'Resim'
    
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='Başlık')
    image = models.ImageField(blank=True, upload_to='images/', verbose_name='Resim')
    
    class Meta:
        verbose_name = 'Resim'
        verbose_name_plural = 'Resimler'

    def __str__(self):
        return self.title
    
    def image_icon(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    
    image_icon.short_description = 'Resim'