from django.contrib import admin
from .models import *
from django.db.models import Q
from django.utils.text import slugify

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['Category_Name']
    list_display = ['Category_Name']
    prepopulated_fields = {"slug": ['Category_Name',]}
admin.site.register(category,CategoryAdmin)



@admin.register(GalleryAlbum)
class ImageAdmin(admin.ModelAdmin):
    
    list_display = (
        'image_file',
        'upload_at'
    )


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['Model_No',]
    list_filter = ['category']
    list_display = ['Model_No', 'Price','category']
    prepopulated_fields = {"slug": ['Model_No',]}

admin.site.register(products, ProductAdmin)
