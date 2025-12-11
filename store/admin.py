from django.contrib import admin
from .models import *
from django.db.models import Q

admin.site.register(category)
admin.site.register(products)


@admin.register(GalleryAlbum)
class ImageAdmin(admin.ModelAdmin):
    
    list_display = (
        'image_file',
        'upload_at'
    )
