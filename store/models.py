from django.db import models
from django_resized import ResizedImageField




class category(models.Model):
    Category_Name = models.CharField(null=False, max_length=50, unique=True)
    Category_Image = models.ImageField(null=False,upload_to='static/media/category')

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.Category_Name

class Hardware(models.Model):
    category = models.ForeignKey(category,on_delete= models.CASCADE)
    Hardware_Image = ResizedImageField(quality = 80,upload_to='static/media/hardware',force_format='WEBP')
    Finish = models.CharField(null=False,max_length=50)
    Material = models.CharField(null=False,max_length=50)
    size = models.CharField(max_length=50)
    Model_No = models.CharField(null=False,max_length=50)
    Price = models.FloatField(null=True,blank=True,max_length=10)

    class Meta:
        verbose_name = "Hardware"
        verbose_name_plural = "Hardwares"

    def __str__(self):
        return self.Model_No
    

class products(models.Model):
    category = models.ForeignKey(category,on_delete= models.CASCADE)
    Product_Image = ResizedImageField(quality = 80,upload_to='static/media/product', force_format='WEBP')
    Color = models.CharField(max_length=50)
    Model_No = models.CharField(max_length=50, null=False, unique=True)
    Size = models.CharField(null=False)
    Material = models.CharField(null=False,max_length=50)
    Finish = models.CharField(null=True,max_length=50)
    Price = models.FloatField(null=True, blank=True,max_length=10)
    Description = models.TextField(blank=True,max_length=100)




    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.Model_No
    

class GalleryAlbum(models.Model):
    image_file = ResizedImageField(quality = 90, upload_to = 'gallery_images', force_format = 'WEBP')
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.image_file} - {self.upload_at}'