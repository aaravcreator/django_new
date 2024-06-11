from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="blogposts")

