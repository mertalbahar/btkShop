from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class ShopSetting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    title = models.CharField(max_length=150, verbose_name='Başlık')
    keywords = models.CharField(max_length=255, verbose_name='Anahtar Kelime')
    description = models.CharField(max_length=255, verbose_name='Açıklama')
    company = models.CharField(max_length=50, verbose_name='Şirket')
    adress = models.CharField(blank=True, max_length=100, verbose_name='Adres')
    phone = models.CharField(blank=True, max_length=15, verbose_name='Telefon')
    fax = models.CharField(blank=True, max_length=15, verbose_name='Faks')
    email = models.CharField(blank=True, max_length=50, verbose_name='Email')
    smtpserver = models.CharField(blank=True, max_length=50, verbose_name='SMTP Sunucu')
    smtpemail = models.CharField(blank=True, max_length=50, verbose_name='SMTP Email')
    smtppassword = models.CharField(blank=True, max_length=10, verbose_name='SMTP Şifre')
    smtpport = models.CharField(blank=True, max_length=5, verbose_name='SMTP Port')
    icon = models.ImageField(blank=True, upload_to='images/', verbose_name='İkon')
    facebook = models.CharField(blank=True, max_length=50, verbose_name='Facebook')
    instagram = models.CharField(blank=True, max_length=50, verbose_name='Instagram')
    linkedin = models.CharField(blank=True, max_length=50, verbose_name='Linkedin')
    twitter = models.CharField(blank=True, max_length=50, verbose_name='Twitter')
    youtube = models.CharField(blank=True, max_length=50, verbose_name='Youtube')
    aboutus = RichTextUploadingField(verbose_name='Hakkımızda')
    contact = RichTextUploadingField(verbose_name='İletişim')
    references = RichTextUploadingField(verbose_name='Referanslar')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='Siteyi Yayınla')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme')
    
    class Meta:
        verbose_name = 'Ayar'
        verbose_name_plural = 'Ayarlar'
    
    def __str__(self):
        return self.title