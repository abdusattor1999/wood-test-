from django.contrib import admin
from .models import Wood, WoodMenu

@admin.register(WoodMenu)
class WoodMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'created_at')
    list_display_links = list_display


@admin.register(Wood)
class WoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'menu',  'created_at')
    list_display_links = list_display

