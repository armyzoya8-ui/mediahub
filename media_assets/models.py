from django.db import models
from django.conf import settings
import cloudinary # madia management - files cloudinary - url - store to the db
from cloudinary.models import CloudinaryField


# Create your models here
class MediaAssets(models.Model):
    CATEGORY_CHOICES =(
        ('image', 'Image') ,
        ('video', 'Video') ,
        ('document' , 'Document') ,

    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='image')
    media_file = CloudinaryField ('media',resource_type='auto',null=True) # cloudinary in use
    # relationship attribute  # object relationship - 'has a' : one user can have many uploads
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='media_assets')
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)
