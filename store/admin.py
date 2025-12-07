from django.contrib import admin
from .models import *

admin.site.register(category)
admin.site.register(products)
admin.site.register(Hardware)

@admin.register(GalleryAlbum)
class ImageAdmin(admin.ModelAdmin):
    
    list_display = (
        'image_file',
        'upload_at'
    )
