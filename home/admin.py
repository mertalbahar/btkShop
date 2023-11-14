from django.contrib import admin
from .models import ShopSetting

@admin.register(ShopSetting)
class ShopSettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
