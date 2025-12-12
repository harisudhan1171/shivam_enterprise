from django.contrib import admin
from .models import *
from django.db.models import Q

admin.site.register(category)



@admin.register(GalleryAlbum)
class ImageAdmin(admin.ModelAdmin):
    
    list_display = (
        'image_file',
        'upload_at'
    )


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['Model_No','category']
    list_filter = ['category']
    list_display = ['Model_No', 'Price','category']

admin.site.register(products, ProductAdmin)
