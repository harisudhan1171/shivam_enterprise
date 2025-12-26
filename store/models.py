from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary.uploader
from django.db.models.signals import post_delete
from django.dispatch import receiver






class category(models.Model):
    Category_Name = models.CharField(null=False, max_length=50, unique=True)
    Category_Image = CloudinaryField('image')
    slug = models.SlugField(default="",null=False)


    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.Category_Name

@receiver(post_delete, sender=category)
def delete_category_image(sender, instance, **kwargs):
    """Delete image from Cloudinary when Product is deleted."""
    try:
        if instance.Category_Image and hasattr(instance.Category_Image, 'public_id'):
            cloudinary.uploader.destroy(instance.Category_Image.public_id)
    except Exception as e:
        print(f"Error deleting image from Cloudinary: {e}") 

    

class products(models.Model):
    category = models.ForeignKey(category,on_delete= models.CASCADE)
    Product_Image = CloudinaryField('image')
    Brand = models.CharField(null=True,blank=True,max_length=50)
    Color = models.CharField(null=True,blank=True,max_length=50)
    Model_No = models.CharField(max_length=50, null=False, unique=True)
    Size = models.CharField(null=False)
    Material = models.CharField(null=False,max_length=50)
    Finish = models.CharField(null=True,max_length=50)
    Price = models.FloatField(null=True, blank=True,max_length=10)
    Thickness = models.CharField(null=True, blank=True,max_length=10)
    Description = models.TextField(blank=True,max_length=100)
    slug = models.SlugField(default="",null=False)



    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.Model_No
    
@receiver(post_delete, sender=products)
def delete_product_image(sender, instance, **kwargs):
    """Delete image from Cloudinary when Product is deleted."""
    try:
        if instance.Product_Image and hasattr(instance.Product_Image, 'public_id'):
            cloudinary.uploader.destroy(instance.Product_Image.public_id)
    except Exception as e:
        print(f"Error deleting image from Cloudinary: {e}")
    

class GalleryAlbum(models.Model):
    image_file = CloudinaryField('image')
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.image_file} - {self.upload_at}'

@receiver(post_delete, sender=GalleryAlbum)
def delete_product_image(sender, instance, **kwargs):
    """Delete image from Cloudinary when Product is deleted."""
    try:
        if instance.image_file and hasattr(instance.image_file, 'public_id'):
            cloudinary.uploader.destroy(instance.image_file.public_id)
    except Exception as e:
        print(f"Error deleting image from Cloudinary: {e}")