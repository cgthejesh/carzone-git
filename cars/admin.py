from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="80" style="border-radius:10px;">'.format(object.car_photo.url))
    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'color', 'year', 'body_style', 'fuel_type')
    list_filter = ('car_title', 'city', 'color', 'body_style', 'fuel_type', 'is_featured')

admin.site.register(Car, CarAdmin)